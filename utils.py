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
            pieces = x.strip().split('\t')
            try:
                song = Songs.select().where(fn.Lower(Songs.title) == fn.Lower(pieces[0])).get()
                col_len = len(pieces)
                only_grade = False
                only_lamp = False
                if col_len < 4:
                    return render_template("import_results.html", result=["Missing both lamp and grade columns"])
                if col_len == 4:
                    if is_grade(pieces[3]):
                        only_grade = True
                    else:
                        only_lamp = True
                chart = Charts.select().where(Charts.difficulty == pieces[1], Charts.song == song.songID).get()
                try:
                    play = ChartStats.select().where(ChartStats.chart == chart.chartID, ChartStats.user).get()
                except:
                    play = ChartStats.create()
                    play.chart = chart.chartID
                    try:
                        play.user = user.userID
                    except Exception as e:
                        print("We're having issues in here: " + str(e))
                play.imported = True
                play.playtype = pieces[2]
                if only_grade:
                    play.grade = pieces[3]
                elif only_lamp:
                    play.lamp = pieces[3]
                else:
                    play.lamp = pieces[3]
                    play.grade = pieces[4]
                play.save()

            except Exception as e:
                print(pieces)
                if 'status' not in failedsongs:
                    failedsongs['status'] = "Following songs failed upload, check spacing. Check title output here with songlist dump from client software";
                    failedsongs['title'] = []
                failedsongs['title'].append(pieces[0])
        if 'status' not in failedsongs:
            failedsongs['status'] = "All songs were added without error"

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

