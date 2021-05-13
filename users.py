from flask import Flask, Markup, request, render_template, json
from bm2dx import app
from models import *

@app.route("/users/all", methods=['GET'])
def list_users():
    users = []
    for user in Users.select():
        users.append(str(user.djname))
    return render_template('userlist.html', users=users)

@app.route("/users", methods=['GET'])
def user():
    #if 'name' in request.args:
        #name = str(request.args['name'])
    #else:
        #return list_users()

    #if name[:3] != "DJ ":
        #name = "DJ " + name


    user = Users.select().limit(1).get()

    plays = Plays.select(Songs.title, Songs.iidx_id, Charts.difficulty, Plays.grade, Plays.lamp, Plays.ex_score).join(Charts).join(Songs, on=(Songs.songID == Charts.song)).order_by(Plays.date.desc()).limit(10).dicts()

    return render_template('userdata.html', name=user.djname, plays=plays)
