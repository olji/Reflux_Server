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
    lampsPerLevel_Percent_unlocked = {}
    gradesPerLevel_Percent_unlocked = {}
    totalLampPerLevel = {}
    totalGradePerLevel = {}
    totalLampPerLevel_unlocked = {}
    totalGradePerLevel_unlocked = {}
    lamppercent = {'l_NP':0, 'l_F':0, 'l_AC':0, 'l_EC':0, 'l_NC':0, 'l_HC':0, 'l_EX':0, 'l_FC':0, 'l_PFC':0, 'NP':0, 'F':0, 'AC':0, 'EC':0, 'NC':0, 'HC':0, 'EX':0, 'FC':0, 'PFC':0}
    gradepercent = {'l_NP':0, 'l_F':0, 'l_E':0, 'l_D':0, 'l_C':0, 'l_B':0, 'l_A':0, 'l_AA':0, 'l_AAA':0, 'NP':0, 'F':0, 'E':0, 'D':0, 'C':0, 'B':0, 'A':0, 'AA':0, 'AAA':0}
    nLamps = 0
    nGrades = 0
    for play in ChartStats.select(Charts.level, ChartStats.lamp, fn.Count(ChartStats.lamp)).join(Charts).group_by(ChartStats.lamp, Charts.level).where(ChartStats.user==user.userID, ChartStats.playtype == playtype, Charts.unlocked == True).dicts():
        if play['level'] not in lampinfo:
            lampinfo[play['level']] = {}
            totalLampPerLevel[play['level']] = 0
            totalLampPerLevel_unlocked[play['level']] = 0

        totalLampPerLevel[play['level']] = totalLampPerLevel[play['level']] + play['lamp")']
        lampinfo[play['level']][play['lamp']] = play['lamp")']
        lamppercent[play['lamp']] += play['lamp")']
        totalLampPerLevel_unlocked[play['level']] = totalLampPerLevel_unlocked[play['level']] + play['lamp")']
        nLamps += play['lamp")']
    for play in ChartStats.select(Charts.level, ChartStats.lamp, fn.Count(ChartStats.lamp)).join(Charts).group_by(ChartStats.lamp, Charts.level).where(ChartStats.user==user.userID, ChartStats.playtype == playtype, Charts.unlocked == False).dicts():
        if play['level'] not in lampinfo:
            lampinfo[play['level']] = {}
            totalLampPerLevel[play['level']] = 0
            totalLampPerLevel_unlocked[play['level']] = 0

        totalLampPerLevel[play['level']] = totalLampPerLevel[play['level']] + play['lamp")']
        lampinfo[play['level']]['l_'+play['lamp']] = play['lamp")']
        lamppercent['l_'+play['lamp']] += play['lamp")']
        nLamps += play['lamp")']

    for play in ChartStats.select(Charts.level, ChartStats.grade, fn.Count(ChartStats.grade)).join(Charts).group_by(ChartStats.grade, Charts.level).where(ChartStats.user==user.userID, ChartStats.playtype == playtype, Charts.unlocked == True).dicts():
        if play['level'] not in gradeinfo:
            gradeinfo[play['level']] = {}
            totalGradePerLevel[play['level']] = 0
            totalGradePerLevel_unlocked[play['level']] = 0

        totalGradePerLevel[play['level']] = totalGradePerLevel[play['level']] + play['grade")']
        gradeinfo[play['level']][play['grade']] = play['grade")']
        gradepercent[play['grade']] += play['grade")']
        totalGradePerLevel_unlocked[play['level']] = totalGradePerLevel_unlocked[play['level']] + play['grade")']
        nGrades += play['grade")']

    for play in ChartStats.select(Charts.level, ChartStats.grade, fn.Count(ChartStats.grade)).join(Charts).group_by(ChartStats.grade, Charts.level).where(ChartStats.user==user.userID, ChartStats.playtype == playtype, Charts.unlocked == False).dicts():
        if play['level'] not in gradeinfo:
            gradeinfo[play['level']] = {}
            totalGradePerLevel[play['level']] = 0
            totalGradePerLevel_unlocked[play['level']] = 0

        totalGradePerLevel[play['level']] = totalGradePerLevel[play['level']] + play['grade")']
        gradeinfo[play['level']]['l_'+play['grade']] = play['grade")']
        gradepercent['l_'+play['grade']] += play['grade")']
        nGrades += play['grade")']

    for item in gradeinfo:
        print(str(item) + ': ' + str(gradeinfo[item]))

    for level in range(13):

        if level == 0: continue
        if level not in lampinfo: continue
        if level not in gradeinfo: continue
        lampsPerLevel_Percent[level] = {}
        gradesPerLevel_Percent[level] = {}
        lampsPerLevel_Percent_unlocked[level] = {}
        gradesPerLevel_Percent_unlocked[level] = {}
        for label in lampinfo[level]:
            if('l_' not in label):
                lampsPerLevel_Percent_unlocked[level][label] = {}
                lampsPerLevel_Percent_unlocked[level][label] = (lampinfo[level][label] / totalLampPerLevel_unlocked[level]) * 100
            lampsPerLevel_Percent[level][label] = {}
            lampsPerLevel_Percent[level][label] = (lampinfo[level][label] / totalLampPerLevel[level]) * 100
        for label in gradeinfo[level]:
            if('l_' not in label):
                gradesPerLevel_Percent_unlocked[level][label] = (gradeinfo[level][label] / totalGradePerLevel_unlocked[level]) * 100
            gradesPerLevel_Percent[level][label] = (gradeinfo[level][label] / totalGradePerLevel[level]) * 100

    return render_template('stats.html', gradepercent=gradepercent, lamppercent=lamppercent, levelgradepercent=gradesPerLevel_Percent, levellamppercent=lampsPerLevel_Percent, levellamppercent_onlyunlocked=lampsPerLevel_Percent_unlocked, levelgradepercent_onlyunlocked=gradesPerLevel_Percent_unlocked)
