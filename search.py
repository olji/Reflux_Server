from bm2dx import app
from flask import Flask, Markup, request, render_template, json, send_from_directory
from models import *

@app.route("/search", methods=['GET', 'POST'])
def searchpage():
    formhist={'mode':"NA", 'name':"", "grade":"NA", "lamp":"NA", "sort":"NA", "sortorder":"asc", 'unlocked':'both'}
    if(request.method == 'POST'):
        query = ChartStats.select().join(Charts).join(Songs)
        formhist={}

        sortReq = ""
        if request.form.get('mode') != "NA":
            mode = str(request.form.get('mode'))
            formhist['mode']=mode
            if(mode == "SP"):
                query = query.where((ChartStats.playtype == "P1") | (ChartStats.playtype == "P2"))
            else:
                query = query.where(ChartStats.playtype == mode)
        if request.form.get('songname') != "":
            name = str(request.form.get('songname'))
            formhist['name']=name
            query = query.where((Songs.title.contains(name)) | (Songs.title2.contains(name)))
        if request.form.get('grade') != "NA":
            grade = str(request.form.get('grade'))
            formhist['grade']=grade
            query = query.where(ChartStats.grade == grade)
        if request.form.get('unlocked') != "both":
            unlocked = str(request.form.get('unlocked'))
            formhist['unlocked']=unlocked
            query = query.where(Charts.unlocked == (True if unlocked=="yes" else False))
        if request.form.get('lamp') != "NA":
            lamp = str(request.form.get('lamp'))
            formhist['lamp']=lamp
            query = query.where(ChartStats.lamp == lamp)
        if request.form.get('sort') != "NA":
            sortParam = None
            sortReq = request.form.get('sort')
            sortdesc = request.form.get('sortorder') == "desc"
            formhist['sort']=sortReq
            formhist['sortorder']=request.form.get('sortorder')
            if(sortReq == "title"):
                sortParam = fn.Lower(Songs.title)
            if(sortReq == "title2"):
                sortParam = fn.Lower(Songs.title2)
            if(sortReq == "level"):
                sortParam = Charts.level
            if(sortReq == "iidx_id"):
                sortParam = Songs.iidx_id
            if(sortReq == "date"):
                sortParam = ChartStats.lastplayed
            if(sortdesc):
                sortParam = -sortParam
            query = query.order_by(sortParam)
        data = []
        charts = []
        for play in query:
            if(sortReq == "title2"):
                charts.append({'songid':play.chart.song.iidx_id, 'title':play.chart.song.title + " (" + play.chart.song.title2 + ")", 'diff':play.chart.difficulty, 'unlocked':play.chart.unlocked, 'level':play.chart.level, 'playdate':play.lastplayed})
            else:
                charts.append({'songid':play.chart.song.iidx_id, 'title':play.chart.song.title, 'diff':play.chart.difficulty, 'unlocked':play.chart.unlocked, 'level':play.chart.level, 'playdate':play.lastplayed})

    else:
        charts = []
    return render_template('search.html', formhist=formhist, data=charts)
