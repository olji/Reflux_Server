from bm2dx import app
from flask import Flask, Markup, request, render_template, json, send_from_directory
from models import *

@app.route("/farm", methods=['GET'])
def farm():
    farmType = None
    target = None
    if 'type' in request.args:
        farmType = str(request.args['type'])
    if 'args' in request.args:
        target = str(request.args['args'])
    if farmType == "grade":
        data = GetSongsForTargetGrade(target)
    elif farmType == "import":
        data = GetImportedPlays()
    elif farmType == "old":
        data = GetOldPlays()

    farmtypes = ["grade", "import", "old"]
    args = {'grade':["A", "AA", "AAA", "MAX"], 'import':[], 'old':["span"], 'generic':["limit", "unique"]}

    rows = {'data':data, 'count':len(data), 'mode':target}

    return render_template('farm.html', data=rows, types=farmtypes, args=args)

def GetOldPlays():
    data = []
    for play in ChartStats.select().join(Charts).join(Songs).group_by(Songs.iidx_id).order_by(ChartStats.lastplayed).limit(200):
        data.append({'title':play.chart.song.title, 'level':play.chart.level, 'songid':play.chart.song.iidx_id, 'diff':play.chart.difficulty, 'current':"", 'criteria_label':"", 'criteria': ""})
    data = sorted(data, key=lambda x: x['level'])
    return data
def GetImportedPlays():
    data = []
    for play in ChartStats.select().join(Charts).join(Songs).where(ChartStats.imported == True):
        data.append({'title':play.chart.song.title, 'level':play.chart.level, 'songid':play.chart.song.iidx_id, 'diff':play.chart.difficulty, 'current':"", 'criteria_label':"", 'criteria': ""})
    data = sorted(data, key=lambda x: x['level'])
    return data

def GetSongsForTargetGrade(target):
    data = []
    targetpercent = 0
    if target == "MAX":
        targetpercent = 1.0
    elif target == "AAA":
        targetpercent = 0.8889
    elif target == "AA":
        targetpercent = 0.7778
    elif target == "A":
        targetpercent = 0.6667
        
    query = ChartStats.select(Songs.title, Songs.iidx_id, Charts.level, Charts.difficulty, ChartStats.grade, Charts.notecount, ChartStats.ex_score, ChartStats.percent_max).join(Charts).join(Songs).where(ChartStats.percent_max < targetpercent)
    query = query.order_by(ChartStats.percent_max.desc())

    for play in query.dicts():
        if grade_lower(play['grade'], target):
            if target == "MAX": 
                data.append({'title':play['title'], 'songid':play['iidx_id'], 'level':play['level'], 'diff':play['difficulty'], 'current':play['grade'], 'criteria_label':"ex_score / MAX", 'criteria': "{:.2f}%".format(play['ex_score'] / (play['notecount'] * 2) * 100)})
            elif target == "AAA": 
                data.append({'title':play['title'], 'songid':play['iidx_id'], 'level':play['level'], 'diff':play['difficulty'], 'current':play['grade'], 'criteria_label':"ex_score / AAA", 'criteria': "{:.2f}%".format(play['ex_score'] / (play['notecount'] * 2 / 9 * 8) * 100)})
            elif target == "AA": 
                data.append({'title':play['title'], 'songid':play['iidx_id'], 'level':play['level'], 'diff':play['difficulty'], 'current':play['grade'], 'criteria_label':"ex_score / AA", 'criteria': "{:.2f}%".format(play['ex_score'] / (play['notecount'] * 2 / 9 * 7) * 100)})
            elif target == "A": 
                data.append({'title':play['title'], 'songid':play['iidx_id'], 'level':play['level'], 'diff':play['difficulty'], 'current':play['grade'], 'criteria_label':"ex_score / A", 'criteria': "{:.2f}%".format(play['ex_score'] / (play['notecount'] * 2 / 9 * 6) * 100)})
    return data

def grade_lower(val, target):
    gradeorder = ["MAX", "AAA", "AA", "A", "B", "C", "D", "E", "F", "NP", ""]
    return gradeorder.index(target) < gradeorder.index(val)
