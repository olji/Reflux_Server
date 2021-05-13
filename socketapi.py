from bm2dx import socket
from flask import Flask, render_template, Markup
from flask_socketio import send, emit
#from flask import Flask, Markup, request, render_template, json, send_from_directory
from models import *

def notify_play():
    play = Plays.select().join(Charts).join(Songs).order_by(Plays.date.desc()).limit(1).get()

    # For testing
    #play = Plays.select().join(Charts).join(Songs).order_by(fn.Random()).limit(1).get()

    grade_divclass = "bcdef"

    if play.grade == "A":
        grade_divclass = "a"
    elif play.grade == "AA":
        grade_divclass = "aa"
    elif play.grade == "AAA" or play.grade == "MAX":
        grade_divclass = "aaa"

    if play.lamp=="FC":
        grade_divclass += "_fc"

    lampclass = "static"
    if(play.lamp == "F" or play.lamp == "EX" or play.lamp == "FC"):
        lampclass = "anim_"+play.lamp


    percentage = (play.ex_score / (play.chart.notecount*2)) * 297
    title = play.chart.song.title + " " + play.chart.difficulty

    fontsize = 30

    socket.emit("newplay", {'title':title, 'defaultFontSize':fontsize, 'lampclass':lampclass, 'divclass':grade_divclass, 'lamp':play.lamp.lower(), 'fillpercentage':percentage}, broadcast=True)

@socket.on('message')
def handle_message(data):
    print('Generic data handler')
    print('received message: ' + data)
    send(message)
@socket.on('json')
def handle_message(json):
    print('Generic json handler')
    print('received json:')
    print(data)
    send(message)

@socket.on('cevent')
def cevent(json):
    print('received message:')
    print(json)
    emit('cresponse', json)