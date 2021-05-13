from flask import Flask, Markup, request, render_template, json
from bm2dx import app
from models import *

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return render_template("import.html")
        file = request.files['file']
        failedsongs = {}
        user = Users.select().where(Users.apikey == request.form['apikey']).get()
        for x in file.readlines():
            x = str(x, "utf-8")
            pieces = x.strip().split(',')
            if(len(pieces) != 6):
                return render_template("import_results.html", result=["File format is wrong"])
            if(pieces[1] == "SPB" or pieces[1] == "DPB"):
                continue
            song = Songs.select().where(Songs.iidx_id == pieces[0]).get()
            try:
                chart = Charts.select().where(Charts.difficulty == pieces[1], Charts.song == song.songID).get()
            except:
                if 'status' not in failedsongs:
                    failedsongs['status'] = "The following songs failed due to missing charts";
                    failedsongs['title'] = []
                failedsongs['title'].append(pieces[0])

            try:
                play = ChartStats.select().where(ChartStats.chart == chart.chartID, ChartStats.user).get()
            except:
                playtype = pieces[1][0:1]
                play = ChartStats.create(chart = chart.chartID, user = user.userID, playtype = playtype)
            play.imported = True
            play.grade = pieces[2]
            play.lamp = pieces[3]
            play.ex_score = pieces[4]
            play.miss = pieces[5]
            play.save()

        return render_template("import_results.html", result=failedsongs)

    return render_template("import.html")

def is_grade(val):
    return val == "F" or val == "E" or val == "D" or val == "C" or val == "B" or val == "A" or val == "AA" or val == "AAA"

# In cases where some part of the software chain screwed up and the ex score doesn't match the grade
#@app.route("/regrade", methods=['GET'])
def regrade_plays():
    data = ChartStats.select().join(Charts)
    for play in data:
        notecount = play.chart.notecount
        ex = play.ex_score

        maxEx = notecount * 2;
        exPart = maxEx / 9;

        if (ex >= exPart * 8):
            newgrade = "AAA";
        elif (ex >= exPart * 7):
            newgrade = "AA";
        elif (ex >= exPart * 6):
            newgrade = "A";
        elif (ex >= exPart * 5):
            newgrade = "B";
        elif (ex >= exPart * 4):
            newgrade = "C";
        elif (ex >= exPart * 3):
            newgrade = "D";
        elif (ex >= exPart * 2):
            newgrade = "E";
        else:
            newgrade = "F";

        print("Setting play " + str(play.playID) + " grade to " + newgrade)
        play.grade = newgrade
        play.save()
    return "All plays have been regraded", 200

