from flask import Flask, Markup, request, render_template, json
from bm2dx import app
from models import *

#@app.route("/plays", methods=['GET'])
def play_page():
    if 'playid' in request.args:
        playid = request.args['playid']
    else:
        return list_plays()

    data = ChartStats.select(Songs.title, Songs.genre, Songs.artist, Songs.bpm, Charts.notecount, Charts.difficulty, Charts.level, ChartStats.grade, ChartStats.lamp, ChartStats.miss, ChartStats.combobreak, ChartStats.ex_score, Users.djname, ChartStats.playtype).join(Charts).join(Songs, on=(Songs.songID == Charts.song)).join(Users, on=(Users.userID == ChartStats.user)).where(ChartStats.playID == playid).dicts().get()
    #data = ChartStats.select(Songs.title, Songs.genre, Songs.artist, Songs.bpm, Charts.notecount, Charts.difficulty, Charts.level, Plays.grade, Plays.lamp, Plays.pgreat, Plays.great, Plays.good, Plays.bad, Plays.poor, Plays.combobreak, Plays.ex_score, Plays.fast, Plays.slow, Plays.gaugepercent, Plays.date, Users.djname, Plays.playtype, Plays.style, Plays.style2, Plays.gauge, Plays.assist, Plays.range).join(Charts).join(Songs, on=(Songs.songID == Charts.song)).join(Users, on=(Users.userID == Plays.user)).where(Plays.playID == playid).dicts().get()

    title=data['title']
    genre=data['genre']
    artist=data['artist']
    bpm=data['bpm']
    notecount=data['notecount']
    diff=data['difficulty']
    level=data['level']
    grade=data['grade']
    lamp=data['lamp']
    pgreat=data['pgreat']
    great=data['great']
    good=data['good']
    bad=data['bad']
    poor=data['poor']
    combobreak=data['combobreak']
    exscore=data['ex_score']
    fast=data['fast']
    slow=data['slow']
    gaugepercent=data['gaugepercent']
    date=data['date']
    user=data['djname']
    playtype=data['playtype']
    if playtype == "DP":
        setting_style=data['style'] + "|" + data['style2']
    else:
        setting_style=data['style']
    setting_gauge=data['gauge']
    setting_assist=data['assist']
    setting_range=data['range']

    grade_divclass = "bcdef"

    if grade == "A":
        grade_divclass = "a"
    elif grade == "AA":
        grade_divclass = "aa"
    elif grade == "AAA" or grade == "MAX":
        grade_divclass = "aaa"

    gauge_divclass = "normal"
    if setting_gauge == "ASSISTED EASY":
        gauge_divclass = "aeasy"
    elif setting_gauge == "HARD":
        gauge_divclass = "hard"
    elif setting_gauge == "EX HARD":
        gauge_divclass = "exhard"

    if lamp=="NP":
        lamp = "NO PLAY"
    elif lamp=="F":
        lamp = "FAIL"
    elif lamp=="AC":
        lamp = "ASSIST CLEAR"
    elif lamp=="EC":
        lamp = "EASY CLEAR"
    elif lamp=="NC":
        lamp = "NORMAL CLEAR"
    elif lamp=="HC":
        lamp = "HARD CLEAR"
    elif lamp=="EX":
        lamp = "EX HARD CLEAR"
    elif lamp=="FC" or lamp == "PFC":
        lamp = "FULL COMBO"
        grade_divclass += "_fc"

    date = date.replace("T", " ")

    percentage = (exscore / (notecount*2)) * 297
    gaugepercentage = (gaugepercent/100) * 302
    grade_div = Markup('<progress class="djlevelbar ' + grade_divclass + '" max="334" value="' + str(percentage+25) + '"></progress>')
    gauge_div = Markup('<progress class="gaugebar ' + gauge_divclass + '" max="302" value="' + str(gaugepercentage) + '"></progress>')
    playdata = {
            'title':title,
            'pbar_grade_html':grade_div,
            'pbar_gauge_html':gauge_div,
            'artist':artist,
            'genre':genre,
            'bpm':bpm,
            'notecount':notecount,
            'diff':diff,
            'level':level,
            'grade':grade,
            'lamp':lamp,
            'pgreat':pgreat,
            'great':great,
            'good':good,
            'bad':bad,
            'poor':poor,
            'combobreak':combobreak,
            'exscore':exscore,
            'fast':fast,
            'slow':slow,
            'playtype':playtype,
            'style':setting_style,
            'gauge':setting_gauge,
            'assist':setting_assist,
            'range':setting_range,
            'date':date,
            'user':user
    }

    return render_template('playdata.html', data=playdata)


#@app.route("/plays/all", methods=['GET'])
def list_plays():
    data = []
    for entry in ChartStats.select(ChartStats.playID, Users.djname, Songs.title, Charts.difficulty, ChartStats.ex_score, ChartStats.lamp, ChartStats.grade).join(Charts).join(Songs, on=(Songs.songID == Charts.song)).join(Users, on=(Users.userID == ChartStats.user)).dicts():
        data.append([entry['playID'], entry['djname'], entry['title'], entry['difficulty'], entry['ex_score'], entry['lamp'], entry['grade'], entry['date']])
    return render_template('playslist.html', plays=data)
