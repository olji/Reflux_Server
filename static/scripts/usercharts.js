function drawStats(lamppercent, gradepercent, levellamppercent, levelgradepercent, levellamppercent_onlyunlocked, levelgradepercent_onlyunlocked){
    var p_np = {label:"NP", data:[], backgroundColor:"#555"};
    var p_flamp = {label:"F", data:[], backgroundColor:"#600"};
    var p_ac = {label:"AC", data:[], backgroundColor:"#f0f"};
    var p_ec = {label:"EC", data:[], backgroundColor:"#0f0"};
    var p_nc = {label:"NC", data:[], backgroundColor:"#0ff"};
    var p_hc = {label:"HC", data:[], backgroundColor:"#f00"};
    var p_ex = {label:"EX", data:[], backgroundColor:"#fa0"};
    var p_fc = {label:"FC", data:[], backgroundColor:"#fcf"};
    var p_pfc = {label:"PFC", data:[], backgroundColor:"#fff"};

    var gp_np = {label:"NP", data:[], backgroundColor:"#555"}
    var p_f = {label:"F", data:[], backgroundColor:"#600"}
    var p_e = {label:"E", data:[], backgroundColor:"#b00"}
    var p_d = {label:"D", data:[], backgroundColor:"#c55"}
    var p_c = {label:"C", data:[], backgroundColor:"#faa"}
    var p_b = {label:"B", data:[], backgroundColor:"#bbb"}
    var p_a = {label:"A", data:[], backgroundColor:"#fc8"}
    var p_aa = {label:"AA", data:[], backgroundColor:"#fa0"}
    var p_aaa = {label:"AAA", data:[], backgroundColor:"#ff0"}

    var locked_p_np = {label:"(Locked) NP", data:[], backgroundColor:"#333"};
    var locked_p_flamp = {label:"(Locked) F", data:[], backgroundColor:"#300"};
    var locked_p_ac = {label:"(Locked) AC", data:[], backgroundColor:"#a0a"};
    var locked_p_ec = {label:"(Locked) EC", data:[], backgroundColor:"#0a0"};
    var locked_p_nc = {label:"(Locked) NC", data:[], backgroundColor:"#0aa"};
    var locked_p_hc = {label:"(Locked) HC", data:[], backgroundColor:"#a00"};
    var locked_p_ex = {label:"(Locked) EX", data:[], backgroundColor:"#a50"};
    var locked_p_fc = {label:"(Locked) FC", data:[], backgroundColor:"#a9a"};
    var locked_p_pfc = {label:"(Locked) PFC", data:[], backgroundColor:"#aaa"};

    var locked_gp_np = {label:"(Locked) NP", data:[], backgroundColor:"#333"}
    var locked_p_f = {label:"(Locked) F", data:[], backgroundColor:"#300"}
    var locked_p_e = {label:"(Locked) E", data:[], backgroundColor:"#b00"}
    var locked_p_d = {label:"(Locked) D", data:[], backgroundColor:"#911"}
    var locked_p_c = {label:"(Locked) C", data:[], backgroundColor:"#a55"}
    var locked_p_b = {label:"(Locked) B", data:[], backgroundColor:"#666"}
    var locked_p_a = {label:"(Locked) A", data:[], backgroundColor:"#a93"}
    var locked_p_aa = {label:"(Locked) AA", data:[], backgroundColor:"#a50"}
    var locked_p_aaa = {label:"(Locked) AAA", data:[], backgroundColor:"#aa0"}


    var only_unlocked_p_nplamp = {label:"NP", data:[], backgroundColor:"#555"};
    var only_unlocked_p_flamp = {label:"F", data:[], backgroundColor:"#600"};
    var only_unlocked_p_ac = {label:"AC", data:[], backgroundColor:"#f0f"};
    var only_unlocked_p_ec = {label:"EC", data:[], backgroundColor:"#0f0"};
    var only_unlocked_p_nc = {label:"NC", data:[], backgroundColor:"#0ff"};
    var only_unlocked_p_hc = {label:"HC", data:[], backgroundColor:"#f00"};
    var only_unlocked_p_ex = {label:"EX", data:[], backgroundColor:"#fa0"};
    var only_unlocked_p_fc = {label:"FC", data:[], backgroundColor:"#fcf"};
    var only_unlocked_p_pfc = {label:"PFC", data:[], backgroundColor:"#fff"};

    var only_unlocked_p_np = {label:"NP", data:[], backgroundColor:"#555"}
    var only_unlocked_p_f = {label:"F", data:[], backgroundColor:"#600"}
    var only_unlocked_p_e = {label:"E", data:[], backgroundColor:"#b00"}
    var only_unlocked_p_d = {label:"D", data:[], backgroundColor:"#c55"}
    var only_unlocked_p_c = {label:"C", data:[], backgroundColor:"#faa"}
    var only_unlocked_p_b = {label:"B", data:[], backgroundColor:"#bbb"}
    var only_unlocked_p_a = {label:"A", data:[], backgroundColor:"#fc8"}
    var only_unlocked_p_aa = {label:"AA", data:[], backgroundColor:"#fa0"}
    var only_unlocked_p_aaa = {label:"AAA", data:[], backgroundColor:"#ff0"}

    for(var level = 1; level < 13; level++ ){

        p_np['data'].push(level in levellamppercent && "NP" in levellamppercent[level] ? levellamppercent[level]["NP"] : 0);
        p_flamp['data'].push(level in levellamppercent && "F" in levellamppercent[level] ? levellamppercent[level]["F"] : 0);
        p_ac['data'].push(level in levellamppercent && "AC" in levellamppercent[level] ? levellamppercent[level]["AC"] : 0);
        p_ec['data'].push(level in levellamppercent && "EC" in levellamppercent[level] ? levellamppercent[level]["EC"] : 0);
        p_nc['data'].push(level in levellamppercent && "NC" in levellamppercent[level] ? levellamppercent[level]["NC"] : 0);
        p_hc['data'].push(level in levellamppercent && "HC" in levellamppercent[level] ? levellamppercent[level]["HC"] : 0);
        p_ex['data'].push(level in levellamppercent && "EX" in levellamppercent[level] ? levellamppercent[level]["EX"] : 0);
        p_fc['data'].push(level in levellamppercent && "FC" in levellamppercent[level] ? levellamppercent[level]["FC"] : 0);
        p_pfc['data'].push(level in levellamppercent && "PFC" in levellamppercent[level] ? levellamppercent[level]["PFC"] : 0);

        gp_np['data'].push(level in levelgradepercent && "NP" in levelgradepercent[level] ? levelgradepercent[level]["NP"] : 0);
        p_f['data'].push(level in levelgradepercent && "F" in levelgradepercent[level] ? levelgradepercent[level]["F"] : 0);
        p_e['data'].push(level in levelgradepercent && "E" in levelgradepercent[level] ? levelgradepercent[level]["E"] : 0);
        p_d['data'].push(level in levelgradepercent && "D" in levelgradepercent[level] ? levelgradepercent[level]["D"] : 0);
        p_c['data'].push(level in levelgradepercent && "C" in levelgradepercent[level] ? levelgradepercent[level]["C"] : 0);
        p_b['data'].push(level in levelgradepercent && "B" in levelgradepercent[level] ? levelgradepercent[level]["B"] : 0);
        p_a['data'].push(level in levelgradepercent && "A" in levelgradepercent[level] ? levelgradepercent[level]["A"] : 0);
        p_aa['data'].push(level in levelgradepercent && "AA" in levelgradepercent[level] ? levelgradepercent[level]["AA"] : 0);
        p_aaa['data'].push(level in levelgradepercent && "AAA" in levelgradepercent[level] ? levelgradepercent[level]["AAA"] : 0);

        locked_p_np['data'].push(level in levellamppercent && "l_NP" in levellamppercent[level] ? levellamppercent[level]["l_NP"] : 0);
        locked_p_flamp['data'].push(level in levellamppercent && "l_F" in levellamppercent[level] ? levellamppercent[level]["l_F"] : 0);
        locked_p_ac['data'].push(level in levellamppercent && "l_AC" in levellamppercent[level] ? levellamppercent[level]["l_AC"] : 0);
        locked_p_ec['data'].push(level in levellamppercent && "l_EC" in levellamppercent[level] ? levellamppercent[level]["l_EC"] : 0);
        locked_p_nc['data'].push(level in levellamppercent && "l_NC" in levellamppercent[level] ? levellamppercent[level]["l_NC"] : 0);
        locked_p_hc['data'].push(level in levellamppercent && "l_HC" in levellamppercent[level] ? levellamppercent[level]["l_HC"] : 0);
        locked_p_ex['data'].push(level in levellamppercent && "l_EX" in levellamppercent[level] ? levellamppercent[level]["l_EX"] : 0);
        locked_p_fc['data'].push(level in levellamppercent && "l_FC" in levellamppercent[level] ? levellamppercent[level]["l_FC"] : 0);
        locked_p_pfc['data'].push(level in levellamppercent && "l_PFC" in levellamppercent[level] ? levellamppercent[level]["l_PFC"] : 0);

        locked_gp_np['data'].push(level in levelgradepercent && "l_NP" in levelgradepercent[level] ? levelgradepercent[level]["l_NP"] : 0);
        locked_p_f['data'].push(level in levelgradepercent && "l_F" in levelgradepercent[level] ? levelgradepercent[level]["l_F"] : 0);
        locked_p_e['data'].push(level in levelgradepercent && "l_E" in levelgradepercent[level] ? levelgradepercent[level]["l_E"] : 0);
        locked_p_d['data'].push(level in levelgradepercent && "l_D" in levelgradepercent[level] ? levelgradepercent[level]["l_D"] : 0);
        locked_p_c['data'].push(level in levelgradepercent && "l_C" in levelgradepercent[level] ? levelgradepercent[level]["l_C"] : 0);
        locked_p_b['data'].push(level in levelgradepercent && "l_B" in levelgradepercent[level] ? levelgradepercent[level]["l_B"] : 0);
        locked_p_a['data'].push(level in levelgradepercent && "l_A" in levelgradepercent[level] ? levelgradepercent[level]["l_A"] : 0);
        locked_p_aa['data'].push(level in levelgradepercent && "l_AA" in levelgradepercent[level] ? levelgradepercent[level]["l_AA"] : 0);
        locked_p_aaa['data'].push(level in levelgradepercent && "l_AAA" in levelgradepercent[level] ? levelgradepercent[level]["l_AAA"] : 0);

        only_unlocked_p_nplamp['data'].push(level in levellamppercent_onlyunlocked && "NP" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["NP"] : 0);
        only_unlocked_p_flamp['data'].push(level in levellamppercent_onlyunlocked && "F" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["F"] : 0);
        only_unlocked_p_ac['data'].push(level in levellamppercent_onlyunlocked && "AC" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["AC"] : 0);
        only_unlocked_p_ec['data'].push(level in levellamppercent_onlyunlocked && "EC" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["EC"] : 0);
        only_unlocked_p_nc['data'].push(level in levellamppercent_onlyunlocked && "NC" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["NC"] : 0);
        only_unlocked_p_hc['data'].push(level in levellamppercent_onlyunlocked && "HC" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["HC"] : 0);
        only_unlocked_p_ex['data'].push(level in levellamppercent_onlyunlocked && "EX" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["EX"] : 0);
        only_unlocked_p_fc['data'].push(level in levellamppercent_onlyunlocked && "FC" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["FC"] : 0);
        only_unlocked_p_pfc['data'].push(level in levellamppercent_onlyunlocked && "PFC" in levellamppercent_onlyunlocked[level] ? levellamppercent_onlyunlocked[level]["PFC"] : 0);

        only_unlocked_p_np['data'].push(level in levelgradepercent_onlyunlocked && "NP" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["NP"] : 0);
        only_unlocked_p_f['data'].push(level in levelgradepercent_onlyunlocked && "F" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["F"] : 0);
        only_unlocked_p_e['data'].push(level in levelgradepercent_onlyunlocked && "E" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["E"] : 0);
        only_unlocked_p_d['data'].push(level in levelgradepercent_onlyunlocked && "D" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["D"] : 0);
        only_unlocked_p_c['data'].push(level in levelgradepercent_onlyunlocked && "C" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["C"] : 0);
        only_unlocked_p_b['data'].push(level in levelgradepercent_onlyunlocked && "B" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["B"] : 0);
        only_unlocked_p_a['data'].push(level in levelgradepercent_onlyunlocked && "A" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["A"] : 0);
        only_unlocked_p_aa['data'].push(level in levelgradepercent_onlyunlocked && "AA" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["AA"] : 0);
        only_unlocked_p_aaa['data'].push(level in levelgradepercent_onlyunlocked && "AAA" in levelgradepercent_onlyunlocked[level] ? levelgradepercent_onlyunlocked[level]["AAA"] : 0);
    }

    var ctx = document.getElementById('lvlgrades_percent');
    var chart = new Chart(ctx, 
        {
            type: 'bar',
            data: {
                labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                datasets: [gp_np,locked_gp_np,p_f,locked_p_f,p_e,locked_p_e,p_d,locked_p_d,p_c,locked_p_c,p_b,locked_p_b,p_a,locked_p_a,p_aa,locked_p_aa,p_aaa,locked_p_aaa] },
            options: {
                legend: {
                    display: false
                },
                scales: {
                    xAxes: [{stacked:true,
                        scaleLabel:{
                            display:true,
                            labelString: "Level"
                        }
                    }],
                    yAxes: [{stacked:true, ticks:{
                        max: 100
                    },
                        scaleLabel:{
                            display:true,
                            labelString: "Percentage"
                        }
                    }]
                }}}
    );

    ctx = document.getElementById('lvlclears_percent');
    var chart2 = new Chart(ctx, 
        {
            type: 'bar',
            data: {
                labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                datasets: [p_np,locked_p_np,p_flamp,locked_p_flamp,p_ac,locked_p_ac,p_ec,locked_p_ec,p_nc,locked_p_nc,p_hc,locked_p_hc,p_ex,locked_p_ex,p_fc,locked_p_fc,p_pfc,locked_p_pfc] },
            options: {
                legend: {
                    display: false
                },
                scales: {
                    xAxes: [{stacked:true,
                        scaleLabel:{
                            display:true,
                            labelString: "Level"
                        }
                    }],
                    yAxes: [{stacked:true, ticks:{
                        max: 100
                    },
                        scaleLabel:{
                            display:true,
                            labelString: "Percentage"
                        }
                    }]
                }}}
    );

    ctx = document.getElementById('lvlgrades_percent_onlyunlocked');
    var chart3 = new Chart(ctx, 
        {
            type: 'bar',
            data: {
                labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                datasets: [only_unlocked_p_np, only_unlocked_p_f, only_unlocked_p_e, only_unlocked_p_d, only_unlocked_p_c, only_unlocked_p_b, only_unlocked_p_a, only_unlocked_p_aa, only_unlocked_p_aaa] },
            options: {
                scales: {
                    xAxes: [{stacked:true,
                        scaleLabel:{
                            display:true,
                            labelString: "Level"
                        }
                    }],
                    yAxes: [{stacked:true, ticks:{
                        max: 100
                    },
                        scaleLabel:{
                            display:true,
                            labelString: "Percentage"
                        }
                    }]
                }}}
    );

    ctx = document.getElementById('lvlclears_percent_onlyunlocked');
    var chart4 = new Chart(ctx, 
        {
            type: 'bar',
            data: {
                labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                datasets: [only_unlocked_p_nplamp, only_unlocked_p_flamp, only_unlocked_p_ac, only_unlocked_p_ec, only_unlocked_p_nc, only_unlocked_p_hc, only_unlocked_p_ex, only_unlocked_p_fc, only_unlocked_p_pfc] },
            options: {
                scales: {
                    xAxes: [{stacked:true,
                        scaleLabel:{
                            display:true,
                            labelString: "Level"
                        }
                    }],
                    yAxes: [{stacked:true, ticks:{
                        max: 100
                    },
                        scaleLabel:{
                            display:true,
                            labelString: "Percentage"
                        }
                    }]
                }}}
    );

    ctx = document.getElementById('grades');
    var chart5 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["(Locked) NP","NP","(Locked) F","F","(Locked) E","E","(Locked) D","D","(Locked) C","C","(Locked) B","B","(Locked) A","A","(Locked) AA","AA","(Locked) AAA","AAA"],
            datasets: [
                {
                    data:[gradepercent["l_NP"],gradepercent["NP"],gradepercent["l_F"],gradepercent["F"],gradepercent["l_E"],gradepercent["E"],gradepercent["l_D"],gradepercent["D"],gradepercent["l_C"],gradepercent["C"],gradepercent["l_B"],gradepercent["B"],gradepercent["l_A"],gradepercent["A"],gradepercent["l_AA"],gradepercent["AA"],gradepercent["l_AAA"],gradepercent["AAA"]],
                    backgroundColor: ["#333","#555","#300","#600","#b00","#b00","#911","#c55","#a55","#faa","#666","#bbb","#a93","#fc8","#a50","#fa0","#aa0","#ff0"]
                }] },
            options: {
                legend: {
                    display: false
                }}
    }
    );

    ctx = document.getElementById('clears');
    var chart6 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["(Locked) NP","NP","(Locked) F","F","(Locked) AC","AC","(Locked) EC","EC","(Locked) NC","NC","(Locked) HC","HC","(Locked) EX","EX","(Locked) FC","FC","(Locked) PFC","PFC"],
            datasets: [{
                data:[lamppercent["l_NP"],lamppercent["NP"],lamppercent["l_F"],lamppercent["F"],lamppercent["l_AC"],lamppercent["AC"],lamppercent["l_EC"],lamppercent["EC"],lamppercent["l_NC"],lamppercent["NC"],lamppercent["l_HC"],lamppercent["HC"],lamppercent["l_EX"],lamppercent["EX"],lamppercent["l_FC"],lamppercent["FC"],lamppercent["l_PFC"],lamppercent["PFC"]],
                backgroundColor: ["#333","#555","#300","#600","#a0a","#f0f","#0a0","#0f0","#0aa","#0ff","#a00","#f00","#a50","#fa0","#a9a","#fcf","#aaa","#fff"]
            }]},
        options: {
            legend: {
                display: false
            }}
    }
    );

    ctx = document.getElementById('grades_onlyunlocked');
    var chart7 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["F", "E", "D", "C", "B", "A", "AA", "AAA"],
            datasets: [
                {
                    data:[gradepercent["F"],gradepercent["E"],gradepercent["D"],gradepercent["C"],gradepercent["B"],gradepercent["A"],gradepercent["AA"],gradepercent["AAA"]],
                    backgroundColor: ["#400","#b00","#c55","#faa","#bbb","#fc8","#fa0","#ff0"]
                }] },
    }
    );

    ctx = document.getElementById('clears_onlyunlocked');
    var chart8 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["F", "AC", "EC", "NC", "HC", "EX", "FC", "PFC"],
            datasets: [{
                data:[lamppercent["F"],lamppercent["AC"],lamppercent["EC"],lamppercent["NC"],lamppercent["HC"],lamppercent["EX"],lamppercent["FC"],lamppercent["PFC"]],
                backgroundColor: ["#400","#f0f","#0f0","#0ff","#f00","#fa0","#fcf","#fff"]
            }]},
    }
    );


}
