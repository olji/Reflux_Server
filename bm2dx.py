from flask import Flask, render_template
from flask_socketio import SocketIO
from functools import cmp_to_key
from models import *
from math import floor
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object('config.ProdConfig')
else:
    app.config.from_object('config.DevConfig')

socket = SocketIO(app)
socket.init_app(app, cors_allowed_origins="*")

@app.route("/", methods=['GET'])
def home():
    unlocked_sp = Charts.select(fn.Count()).where(Charts.unlocked == True, Charts.difficulty % "SP*").scalar()
    unlocked_dp = Charts.select(fn.Count()).where(Charts.unlocked == True, Charts.difficulty % "DP*").scalar()
    unlocked = Charts.select(fn.Count()).where(Charts.unlocked == True).scalar()
    total_sp = Charts.select(fn.Count()).where(Charts.difficulty % "SP*").scalar()
    total_dp = Charts.select(fn.Count()).where(Charts.difficulty % "DP*").scalar()
    hidden_sp = Charts.select(fn.Count()).join(Songs).where(Charts.unlocked == False, Charts.difficulty % "SP*", Songs.unlocktype == "Sub").scalar()
    hidden_dp = Charts.select(fn.Count()).join(Songs).where(Charts.unlocked == False, Charts.difficulty % "DP*", Songs.unlocktype == "Sub").scalar()
    hidden = Charts.select(fn.Count()).join(Songs).where(Charts.unlocked == False, Songs.unlocktype == "Sub").scalar()
    bit_cost = 0;
    for chart in Charts.select().join(Songs).where(Charts.unlocked == False, Songs.unlocktype == "Bits"):
        bit_cost += chart.level * 500
    return render_template('index.html', data={'unlocked_sp':unlocked_sp, 'total_sp':total_sp, 'hidden_sp':hidden_sp, 'unlocked_dp':unlocked_dp, 'total_dp':total_dp, 'hidden_dp':hidden_dp, 'bitcost':bit_cost})

import users
import plays
import songs
import farm
import search
import api
import stats
import utils
import socketapi

from socketapi import notify_play

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route("/justplayed", methods=['GET'])
def spage():
    return render_template('liveplays.html')
@app.route("/ping", methods=['GET'])
def ping():
    notify_play()
    return render_template("404.html")
