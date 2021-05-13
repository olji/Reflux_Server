from bm2dx import app
from flask import Flask, Markup, request, render_template, json, send_from_directory
from models import *

@app.route("/songs", methods=['GET'])
def song():
    print("inside song()")
    diff = None
    if 'songid' in request.args:
        songid = str(request.args['songid'])
    else:
        return list_songs()
    if 'diff' in request.args:
        diff = str(request.args['diff'])

    song = Songs.select().where(Songs.iidx_id == songid).get()
    songdata = {'genre':song.genre, 'title':song.title, 'title2':song.title2, 'artist':song.artist, 'bpm':song.bpm}

    print(diff)
    if diff is None:
        plays = ChartStats.select().join(Charts).join(Users, on=(ChartStats.user == Users.userID)).join(Songs, on=(Songs.songID == Charts.song)).where(Songs.iidx_id == songid)
    else:
        plays = ChartStats.select().join(Charts).join(Users, on=(ChartStats.user == Users.userID)).join(Songs, on=(Songs.songID == Charts.song)).where(Songs.iidx_id == songid, Charts.difficulty == diff)


    entries = []
    for play in plays:
        name = play.user.djname
        playid = play.playID
        diff = play.chart.difficulty
        grade = play.grade
        lamp = play.lamp
        exscore = play.ex_score
        notecount = play.chart.notecount
        if exscore == None:
            exscore = 0
        if lamp == "NP":
            continue;

        grade_divclass = "bcdef"

        if grade == "A":
            grade_divclass = "a"
        elif grade == "AA":
            grade_divclass = "aa"
        elif grade == "AAA" or grade == "MAX":
            grade_divclass = "aaa"

        if lamp=="FC":
            grade_divclass += "_fc"

        percentage = (exscore / (notecount*2)) * 297

        lampclass = "static"
        if(play.lamp == "F" or play.lamp == "EX" or play.lamp == "FC"):
            lampclass = "anim_"+play.lamp

        entries.append({'name':name, 'playid':playid, 'diff':diff, 'grade':grade, 'lamp':lamp.lower(), 'exscore':exscore, 'lampclass':lampclass, 'fillpercentage':percentage, 'divclass':grade_divclass})

    return render_template('songdata.html', songdata=songdata, plays=entries)

@app.route("/songs/all", methods=['GET'])
def list_songs():

    songs = {'abcd':[],'efgh':[],'ijkl':[],'mnop':[],'qrst':[],'uvwxyz':[], 'others':[]}
    groups = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwxyz']
    for song in Songs.select().group_by(Songs.iidx_id).order_by(fn.Lower(Songs.title)):
        group_arr = [x for x in groups if song.title[0].lower() in x]
        if len(group_arr) == 0:
            group = 'others'
        else:
            group = group_arr[0]

        firstchar = song.title[0]
        songid = song.songID

        songs[group].append({'title': song.title, 'title2':song.title2, 'songid':song.iidx_id})

    songs['others'] = sorted(songs['others'], key=lambda x: x['title2'].lower())

    return render_template('songlist.html', songs=songs)
