from flask import Flask, Markup, request, render_template, json
from bm2dx import app
from models import *

@app.route("/stats", methods=['GET'])
def show_stats():

    user = Users.select().limit(1).get()

    playtype = 'SP'
    if 'playtype' in request.args:
        playtype = str(request.args['playtype'])
    lvlgrades = {}
    lvlgrades['labels'] = []
    labels = []
    grades = ['F', 'E', 'D', 'C', 'B', 'A', 'AA', 'AAA']
    lamps = ['NP', 'F', 'AC', 'EC', 'NC', 'HC', 'EX', 'FC', 'PFC']
    gradescolor = ['#400', '#b00', '#c55', '#faa', '#bbb', '#fc8', '#fa0', '#ff0']
    lampscolor = ['#444', '#400', '#f0f', '#0f0', '#0ff', '#f00', '#fa0', '#fcf', "#fff"]
    datasets = []

    lampinfo = {}
    gradeinfo = {}
    lampsPerLevel_Percent = {}
    gradesPerLevel_Percent = {}
    lampsPerLevel_Percent_op = {}
    gradesPerLevel_Percent_op = {}
    totalLampPerLevel = {}
    totalGradePerLevel = {}
    totalLampPerLevel_op = {}
    totalGradePerLevel_op = {}
    lamppercent = {'NP':0, 'F':0, 'AC':0, 'EC':0, 'NC':0, 'HC':0, 'EX':0, 'FC':0, 'PFC':0}
    gradepercent = {'NP':0, 'F':0, 'E':0, 'D':0, 'C':0, 'B':0, 'A':0, 'AA':0, 'AAA':0}
    nLamps = 0
    nGrades = 0
    for play in ChartStats.select(Charts.level, ChartStats.lamp, fn.Count(ChartStats.lamp)).join(Charts).group_by(ChartStats.lamp, Charts.level).where(ChartStats.user==user.userID, ChartStats.playtype == playtype).dicts():
        if play['level'] not in lampinfo:
            lampinfo[play['level']] = {}
            totalLampPerLevel[play['level']] = 0
            totalLampPerLevel_op[play['level']] = 0
        lampinfo[play['level']][play['lamp']] = play['lamp")']
        lamppercent[play['lamp']] += play['lamp")']
        if(play['lamp'] != "NP"):
            totalLampPerLevel_op[play['level']] = totalLampPerLevel[play['level']] + play['lamp")']
        totalLampPerLevel[play['level']] = totalLampPerLevel[play['level']] + play['lamp")']
        nLamps += play['lamp")']
    for play in ChartStats.select(Charts.level, ChartStats.grade, fn.Count(ChartStats.grade)).join(Charts).group_by(ChartStats.grade, Charts.level).where(ChartStats.user==user.userID, ChartStats.playtype == playtype).dicts():
        if play['level'] not in gradeinfo:
            gradeinfo[play['level']] = {}
            totalGradePerLevel[play['level']] = 0
            totalGradePerLevel_op[play['level']] = 0
        gradeinfo[play['level']][play['grade']] = play['grade")']
        gradepercent[play['grade']] += play['grade")']
        if(play['grade'] != "NP"):
            totalGradePerLevel_op[play['level']] = totalGradePerLevel[play['level']] + play['grade")']
        totalGradePerLevel[play['level']] = totalGradePerLevel[play['level']] + play['grade")']
        nGrades += play['grade")']

    for level in range(13):

        if level == 0: continue
        if level not in lampinfo: continue
        if level not in gradeinfo: continue
        lampsPerLevel_Percent[level] = {}
        gradesPerLevel_Percent[level] = {}
        lampsPerLevel_Percent_op[level] = {}
        gradesPerLevel_Percent_op[level] = {}
        for label in lampinfo[level]:
            if(label != "NP"):
                lampsPerLevel_Percent_op[level][label] = {}
                lampsPerLevel_Percent_op[level][label] = (lampinfo[level][label] / totalLampPerLevel_op[level]) * 100
            lampsPerLevel_Percent[level][label] = {}
            lampsPerLevel_Percent[level][label] = (lampinfo[level][label] / totalLampPerLevel[level]) * 100
        for label in gradeinfo[level]:
            if(label != "NP"):
                gradesPerLevel_Percent_op[level][label] = (gradeinfo[level][label] / totalGradePerLevel_op[level]) * 100
            gradesPerLevel_Percent[level][label] = (gradeinfo[level][label] / totalGradePerLevel[level]) * 100

    return render_template('stats.html', gradepercent=gradepercent, lamppercent=lamppercent, levelgradepercent=gradesPerLevel_Percent, levellamppercent=lampsPerLevel_Percent, levellamppercent_onlyplayed=lampsPerLevel_Percent_op, levelgradepercent_onlyplayed=gradesPerLevel_Percent_op)
