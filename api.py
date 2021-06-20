from bm2dx import app
from flask import Flask, Markup, request, render_template, json, send_from_directory
from datetime import date, datetime
from models import *
import os

from socketapi import notify_play
import utils

def validate_apikey(apikey):
     return Users.select(fn.Count(Users.userID)).where(Users.apikey == apikey).get() != 0

@app.route("/api/songplayed", methods=['POST'])
def song_add_entry():
    if 'apikey' not in request.form:
        return "No API key given", 400

    apikey = request.form["apikey"]

    if validate_apikey(apikey) == False:
        return "Invalid api key", 400

    # {{{ Validate post request

    if 'title' not in request.form:
        return "Title not given", 400
    if 'title2' not in request.form:
        return "Title2 not given", 400
    if 'grade' not in request.form:
        return "Grade not given", 400
    if 'lamp' not in request.form:
        return "Lamp not given", 400
    if 'bpm' not in request.form:
        return "Bpm not given", 400
    if 'diff' not in request.form:
        return "Difficulty not given", 400
    if 'artist' not in request.form:
        return "Artist not given", 400
    if 'genre' not in request.form:
        return "Genre not given", 400
    if 'level' not in request.form:
        return "Level not given", 400
    if 'notecount' not in request.form:
        return "Note count not given", 400
    if 'playtype' not in request.form:
        return "Playtype not given", 400
    if 'style' not in request.form:
        return "style not given", 400
    if 'style2' not in request.form:
        return "style2 not given", 400
    if 'assist' not in request.form:
        return "assist not given", 400
    if 'range' not in request.form:
        return "range not given", 400
    if 'exscore' not in request.form:
        return "Exscore not given", 400
    if 'bad' not in request.form:
        return "Bad not given", 400
    if 'poor' not in request.form:
        return "Poor not given", 400
    if 'combobreak' not in request.form:
        return "Combobreak not given", 400
    if 'prematureend' not in request.form:
        return "Premature end information not given", 400
    if 'gauge' not in request.form:
        return "gauge not given", 400
    if not request.form['notecount'].isnumeric():
        return "Notecount is not a number", 400
    if not request.form['level'].isnumeric():
        return "Level is not a number", 400
    if request.form['grade'].upper() not in ['F','E','D','C','B','A','AA','AAA']:
        return "Grade malformed (Accepted grades: [F,E,D,C,B,A,AA,AAA])", 400
    if request.form['lamp'].upper() not in ['NP', 'F', 'AC', 'EC', 'NC', 'HC', 'EX', 'FC', 'PFC']:
        return "Lamp malformed (Accepted lamps: [NP, F, AC, EC NC, HC, EX, FC, PFC])", 400
    if request.form['diff'].upper() not in ['SPB', 'SPN', 'SPH', 'SPA', 'SPL', 'DPB', 'DPN', 'DPH', 'DPA', 'DPL']:
        return "Difficulty malformed (Accepted difficulties: [SPB, SPN, SPH, SPA, SPL, DPB, DPN, DPH, DPA, DPL])", 400
    if int(request.form['level']) > 12 or int(request.form['level']) < 1:
        return "Level outside of range", 400
    # isnumeric() won't work since gauge percent can be negative when failing hard or ex-hard
    try:
        gaugepercent = int(request.form['gaugepercent'])
    except:
        return "gauge percent not given", 400
    # }}}

    # {{{ Fetch play information

    # Song / chart information
    title = request.form['title']
    title2 = request.form['title2']
    songid = request.form['songid']
    bpm = request.form['bpm']
    genre = request.form['genre']
    artist = request.form['artist']
    diff = request.form['diff']
    level = int(request.form['level'])
    notecount = int(request.form['notecount'])

    # Score data
    exscore = int(request.form['exscore'])
    grade = request.form['grade']
    lamp = request.form['lamp']
    playtype = "DP" if "DP" in request.form['playtype'] else "SP"
    gaugetype = request.form['gauge']

    # Clear metadata
    gaugepercent = int(request.form['gaugepercent'])
    style = request.form['style']
    style2 = request.form['style2']
    assist = request.form['assist']
    range_opt = request.form['range']

    # Judge data
    pgreat = int(request.form['pgreat'])
    great = int(request.form['great'])
    good = int(request.form['good'])
    bad = int(request.form['bad'])
    poor = int(request.form['poor'])
    fast = int(request.form['fast'])
    slow = int(request.form['slow'])
    combobreak = int(request.form['combobreak'])
    premature_end = bool(request.form['prematureend'])

    # }}}

    # {{{ Add song / chart if missing in database

    songcount = Songs.select(fn.count(Songs.title)).where(Songs.iidx_id == songid).scalar()


    if songcount == 0:
        eh = add_song(request.form)
    elif songcount >= 2:
        print(str(songcount) + " instances of songs is present in database")
        # Something screwy is going on...

    chartcount = Charts.select(fn.count(Charts.difficulty)).join(Songs).where(Songs.iidx_id == songid.strip(), Charts.difficulty == diff).scalar()

    if chartcount == 0:
        add_chart(request.form)

    # }}}

    userid = Users.select(Users.userID).where(Users.apikey == apikey).get()

    chart = Charts.select(Charts.chartID, Charts.notecount).join(Songs).where(Songs.iidx_id == songid.strip(), Charts.difficulty == diff).get()
    chartid = chart.chartID
    db_notecount = chart.notecount

    # Update notecount if it previously might have been badly fetched on initial insertion
    # Client should be making sure everything is initialized and loaded properly before fetching this data
    if(db_notecount < notecount):
        chart.notecount = notecount
        chart.save()
        print("Updated notecount of chart " + str(chart.chartID) + " to " + str(notecount))

    # {{{ Add new play entry
    play = Plays.create(chart = chartid, user = userid, playtype = playtype)
    play.grade = grade
    play.lamp = lamp
    play.ex_score = exscore
    play.combobreak = combobreak

    play.pgreat = pgreat
    play.great = great
    play.good = good
    play.bad = bad
    play.poor = poor
    play.misscount = bad + poor
    play.fast = fast
    play.slow = slow

    play.gaugepercent = gaugepercent
    play.premature_end = premature_end
    play.style = style
    play.style2 = style2
    play.assist = assist
    play.range_opt = range_opt
    play.gaugetype = gaugetype
    play.date = datetime.now()
    play.save()


    # }}}
    if assist != "OFF":
        "Play saved, assist option used", 200

    # Update top stats for chart
    previousplay = ChartStats.select(fn.count(ChartStats.grade)).where(ChartStats.chart == chartid, ChartStats.user == userid, ChartStats.playtype == playtype).scalar()

    if previousplay == 0:
        # {{{ Handle potential occurences where no stat entry for the chart exist
        chartstat = ChartStats.create(chart = chartid, user=userid, playtype = playtype)
        chartstat.chart = chartid
        chartstat.user = userid
        chartstat.grade = grade
        chartstat.lamp = lamp
        if premature_end:
            chartstat.miss = None
            chartstat.combobreak = None
        else:
            chartstat.miss = bad + poor
            chartstat.combobreak = combobreak
        chartstat.percent_max = exscore / (notecount * 2)
        chartstat.ex_score = exscore
        chartstat.lastplayed = str(date.today())
        chartstat.playtype = playtype
        if gaugetype == "OFF":
            chartstat.nc_gauge = gaugepercent
            chartstat.hc_gauge = 0
            chartstat.ex_gauge = 0
        elif gaugetype == "HARD":
            chartstat.hc_gauge = gaugepercent
            chartstat.nc_gauge = 0
            chartstat.ex_gauge = 0
        elif gaugetype == "EX HARD":
            chartstat.nc_gauge = 0
            chartstat.hc_gauge = 0
            chartstat.ex_gauge = gaugepercent
        chartstat.save()
        # }}}
    else:
        chartstat = ChartStats.select().where(ChartStats.chart == chartid, ChartStats.user == userid, ChartStats.playtype == playtype).get()

        chartstat.grade = grade_max(grade, chartstat.grade)
        chartstat.lamp = lamp_max(lamp, chartstat.lamp)
        if chartstat.imported == True: # If imported, overwrite existing data
            # {{{ Overwrite imported information
            if premature_end:
                chartstat.miss = None
                chartstat.combobreak = None
            else:
                chartstat.miss = bad + poor
                chartstat.combobreak = combobreak
            chartstat.ex_score = exscore
            chartstat.percent_max = exscore / (notecount * 2)
            chartstat.lastplayed = str(date.today())
            chartstat.imported = False
            if gaugetype == "OFF":
                chartstat.nc_gauge = gaugepercent
            elif gaugetype == "HARD":
                chartstat.hc_gauge = gaugepercent
            elif gaugetype == "EX HARD":
                chartstat.ex_gauge = gaugepercent
                # }}}
        else: # If not imported, save the best result on each field
            # {{{ Save new best
            if not premature_end:
                if chartstat.miss == None:
                    chartstat.miss = bad + poor
                else:
                    chartstat.miss = min(bad + poor, chartstat.miss)
                if chartstat.combobreak == None:
                    chartstat.combobreak = combobreak
                else:
                    chartstat.combobreak = min(combobreak, chartstat.combobreak)
            chartstat.ex_score = max(exscore, chartstat.ex_score)
            chartstat.lastplayed = str(date.today())
            chartstat.percent_max = chartstat.ex_score / (notecount * 2)
            if gaugetype == "OFF":
                if chartstat.nc_gauge is None:
                    chartstat.nc_gauge = gaugepercent
                else:
                    if not premature_end:
                        chartstat.nc_gauge = max(gaugepercent, chartstat.nc_gauge)
            elif gaugetype == "HARD":
                if chartstat.hc_gauge is None:
                    chartstat.hc_gauge = gaugepercent
                else:
                    if not premature_end:
                        chartstat.hc_gauge = max(gaugepercent, chartstat.hc_gauge)
            elif gaugetype == "EX HARD":
                if chartstat.ex_gauge is None:
                    chartstat.ex_gauge = gaugepercent
                else:
                    if not premature_end:
                        chartstat.ex_gauge = max(gaugepercent, chartstat.ex_gauge)
            # }}}
        chartstat.save()

    notify_play()
    return "Added entry", 200

# {{{ Adding song and chart 
@app.route("/api/addsong", methods=['POST'])
def update_song():
    apikey = request.form['apikey']
    if validate_apikey(apikey) == False:
        return "Invalid api key", 400
    song = request.form
    songcount = Songs.select(fn.count(Songs.title)).where(Songs.iidx_id == song['songid'].strip()).scalar()
    if songcount == 0:
        add_song(song)
    else:
        s = Songs.select().where(Songs.iidx_id == song['songid'].strip()).get()
        s.iidx_id = song['songid'].strip()
        s.unlocktype = song['unlockType'].strip()
        s.title = song['title'].strip()
        s.title2 = song['title2'].strip()
        s.genre = song['genre'].strip()
        s.artist = song['artist'].strip()
        s.bpm = song['bpm'].strip()
        s.save()

    return "Added song successfully", 200

def add_song(song):
    songcount = Songs.select(fn.count(Songs.title)).where(Songs.iidx_id == song['songid'].strip()).scalar()
    if songcount == 0:
        s = Songs.create()
        s.iidx_id = song['songid'].strip()
        s.title = song['title'].strip()
        s.unlocktype = song['unlockType'].strip()
        s.title2 = song['title2'].strip()
        s.genre = song['genre'].strip()
        s.artist = song['artist'].strip()
        s.bpm = song['bpm'].strip()
        s.save()

@app.route("/api/addchart", methods=['POST'])
def update_chart():
    apikey = request.form['apikey']
    if validate_apikey(apikey) == False:
        return "Invalid api key", 400
    chart = request.form

    chartcount = Charts.select(fn.count(Charts.difficulty)).join(Songs).where(Songs.iidx_id == chart['songid'].strip(), Charts.difficulty == chart['diff'].strip()).scalar()
    if chartcount == 0:
        add_chart(request.form)

    else:
        c = Charts.select().join(Songs).where(Songs.iidx_id == chart['songid'].strip(), Charts.difficulty == chart['diff'].strip()).get()
        c.difficulty = chart['diff'].strip()
        c.level = chart['level'].strip()
        c.notecount = chart['notecount'].strip()
        b = 1 if chart['unlocked'] == "True" else 0
        c.unlocked = b
        c.save()
    return "Added chart successfully", 200

def add_chart(chart):
    chartcount = Charts.select(fn.count(Charts.difficulty)).join(Songs).where(Songs.iidx_id == chart['songid'].strip(), Charts.difficulty == chart['diff'].strip()).scalar()
    if chartcount == 0:
        song = Songs.select().where(Songs.iidx_id == chart['songid']).get()
        c = Charts.create(song_id = song.songID, difficulty = chart['diff'].strip(), level = int(chart['level'].strip()), notecount = int(chart['notecount'].strip()))
        b = 1 if chart['unlocked'] == "True" else 0
        c.unlocked = b
        c.save()

        playtype = "SP" if "SP" in chart['diff'] else "DP"
        cs = ChartStats.create(chart_id = c.chartID, user_id = 1, playtype = playtype)
        cs.grade = "NP"
        cs.lamp = "NP"
        cs.miss = None
        cs.combobreak = None
        cs.ex_score = 0
        cs.nc_gauge = 0
        cs.hc_gauge = 0
        cs.ex_gauge = 0
        cs.percent_max = 0
        cs.save()


@app.route("/api/postscore", methods=['POST'])
def post_score():
    apikey = request.form['apikey']
    if validate_apikey(apikey) == False:
        return "Invalid api key", 400
    form = request.form
    chart = Charts.select().join(Songs).where(Songs.iidx_id == form['songid'].strip(), Charts.difficulty == form['diff'].strip()).get()
    cs = ChartStats.select().where(ChartStats.chart_id == chart.chartID, ChartStats.user_id == 1).get()
    cs.ex_score = int(form['exscore'])
    cs.miss = int(form['misscount'])
    cs.grade = form['grade']
    cs.lamp = form['lamp']
    cs.percent_max = cs.ex_score / (chart.notecount * 2)
    cs.save()
    return "Chart scores updated successfully", 200

# }}}

# {{{ Utility functions
#@app.route("/api/updateEntries", methods=['GET'])
def update_entries():
    for play in ChartStats.select().join(Charts):
        notecount = play.chart.notecount
        play.percent_max = play.ex_score / (notecount * 2)
        play.save()

    print("Finished properly")
    return "done"

#@app.route("/api/genStats", methods=['GET'])
def genstats():
    for chart in Charts.select().join(ChartStats, JOIN.LEFT_OUTER).where(ChartStats.playID == None):
        if "SP" in chart.difficulty:
            playtype = "SP"
        elif "DP" in chart.difficulty:
            playtype = "DP"
        cs = ChartStats.create(chart_id = chart.chartID, user_id = 1, playtype = playtype)
        cs.grade = "NP"
        cs.lamp = "NP"
        cs.miss = None
        cs.combobreak = None
        cs.ex_score = 0
        cs.nc_gauge = 0
        cs.hc_gauge = 0
        cs.ex_gauge = 0
        cs.percent_max = 0
        cs.save()
    print("Everything done")
# }}}

# {{{ Unlock management

@app.route("/api/updatesong", methods=['POST'])
def updateSong():
    apikey = request.form['apikey']
    if validate_apikey(apikey) == False:
        return "Invalid api key", 400

    songid = request.form['songid'].strip()
    unlocktype = request.form['unlockType'].strip()
    for song in Songs.select().where(Songs.iidx_id == songid):
        print("updating " + song.title + " to " + unlocktype)
        song.unlocktype = unlocktype
        song.save()
    return "Song unlock type updated", 200

@app.route("/api/unlocksong", methods=['POST'])
def unlockSong():
    apikey = request.form['apikey']
    if validate_apikey(apikey) == False:
        return "Invalid api key", 400

    songid = request.form['songid'].strip()
    state = int(request.form['state'])
    for chart in Charts.select().join(Songs).where(Songs.iidx_id == songid):
        bit = 1
        if chart.difficulty == "SPN":
            bit = bit << 1;
        elif chart.difficulty == "SPH":
            bit = bit << 2;
        elif chart.difficulty == "SPA":
            bit = bit << 3;
        elif chart.difficulty == "DPN":
            bit = bit << 6;
        elif chart.difficulty == "DPH":
            bit = bit << 7;
        elif chart.difficulty == "DPA":
            bit = bit << 8;
        chart.unlocked = 1 if bit & state > 0 else 0
        chart.save()
    return "Unlock status updated for song " + songid, 200

# }}}

def grade_max(lhs, rhs):
    gradeorder = ["AAA", "AA", "A", "B", "C", "D", "E", "F", ""]
    for grade in gradeorder:
        if lhs == grade or rhs == grade:
            return grade
    return ""
def lamp_max(lhs, rhs):
    lamporder = ["PFC", "FC", "EX", "HC", "NC", "EC", "AC", "F", "NP", ""]
    for lamp in lamporder:
        if lhs == lamp or rhs == lamp:
            return lamp
    return ""

