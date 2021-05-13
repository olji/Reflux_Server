
function drawUserGraphs(lamppercent, gradepercent, levellamppercent, levelgradepercent){
    var p_np = {label:"NP", data:[], backgroundColor:"#444"};
    var p_flamp = {label:"F", data:[], backgroundColor:"#400"};
    var p_ac = {label:"AC", data:[], backgroundColor:"#f0f"};
    var p_ec = {label:"EC", data:[], backgroundColor:"#0f0"};
    var p_nc = {label:"NC", data:[], backgroundColor:"#0ff"};
    var p_hc = {label:"HC", data:[], backgroundColor:"#f00"};
    var p_ex = {label:"EX", data:[], backgroundColor:"#fa0"};
    var p_fc = {label:"FC", data:[], backgroundColor:"#fcf"};

    var gp_np = {label:"NP", data:[], backgroundColor:"#444"}
    var p_f = {label:"F", data:[], backgroundColor:"#400"}
    var p_e = {label:"E", data:[], backgroundColor:"#b00"}
    var p_d = {label:"D", data:[], backgroundColor:"#c55"}
    var p_c = {label:"C", data:[], backgroundColor:"#faa"}
    var p_b = {label:"B", data:[], backgroundColor:"#bbb"}
    var p_a = {label:"A", data:[], backgroundColor:"#fc8"}
    var p_aa = {label:"AA", data:[], backgroundColor:"#fa0"}
    var p_aaa = {label:"AAA", data:[], backgroundColor:"#ff0"}

    for(var level = 1; level < 13; level++ ){

        p_np['data'].push(level in levellamppercent && "NP" in levellamppercent[level] ? levellamppercent[level]["NP"] : 0);
        p_flamp['data'].push(level in levellamppercent && "F" in levellamppercent[level] ? levellamppercent[level]["F"] : 0);
        p_ac['data'].push(level in levellamppercent && "AC" in levellamppercent[level] ? levellamppercent[level]["AC"] : 0);
        p_ec['data'].push(level in levellamppercent && "EC" in levellamppercent[level] ? levellamppercent[level]["EC"] : 0);
        p_nc['data'].push(level in levellamppercent && "NC" in levellamppercent[level] ? levellamppercent[level]["NC"] : 0);
        p_hc['data'].push(level in levellamppercent && "HC" in levellamppercent[level] ? levellamppercent[level]["HC"] : 0);
        p_ex['data'].push(level in levellamppercent && "EX" in levellamppercent[level] ? levellamppercent[level]["EX"] : 0);
        p_fc['data'].push(level in levellamppercent && "FC" in levellamppercent[level] ? levellamppercent[level]["FC"] : 0);

        gp_np['data'].push(level in levelgradepercent && "NP" in levelgradepercent[level] ? levelgradepercent[level]["NP"] : 0);
        p_f['data'].push(level in levelgradepercent && "F" in levelgradepercent[level] ? levelgradepercent[level]["F"] : 0);
        p_e['data'].push(level in levelgradepercent && "E" in levelgradepercent[level] ? levelgradepercent[level]["E"] : 0);
        p_d['data'].push(level in levelgradepercent && "D" in levelgradepercent[level] ? levelgradepercent[level]["D"] : 0);
        p_c['data'].push(level in levelgradepercent && "C" in levelgradepercent[level] ? levelgradepercent[level]["C"] : 0);
        p_b['data'].push(level in levelgradepercent && "B" in levelgradepercent[level] ? levelgradepercent[level]["B"] : 0);
        p_a['data'].push(level in levelgradepercent && "A" in levelgradepercent[level] ? levelgradepercent[level]["A"] : 0);
        p_aa['data'].push(level in levelgradepercent && "AA" in levelgradepercent[level] ? levelgradepercent[level]["AA"] : 0);
        p_aaa['data'].push(level in levelgradepercent && "AAA" in levelgradepercent[level] ? levelgradepercent[level]["AAA"] : 0);
    }


    var ctx = document.getElementById('lvlgrades_percent');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            datasets: [gp_np, p_f, p_e, p_d, p_c, p_b, p_a, p_aa, p_aaa] },
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

    ctx = document.getElementById('lvlclears_percent');
    var chart2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            datasets: [p_np, p_flamp, p_ac, p_ec, p_nc, p_hc, p_ex, p_fc] },
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
            labels: ["NP", "F", "E", "D", "C", "B", "A", "AA", "AAA"],
            datasets: [
		    {
			    data:[gradepercent["NP"],gradepercent["F"],gradepercent["E"],gradepercent["D"],gradepercent["C"],gradepercent["B"],gradepercent["A"],gradepercent["AA"],gradepercent["AAA"]],
			    backgroundColor: ["#444","#400","#b00","#c55","#faa","#bbb","#fc8","#fa0","#ff0"]
		    }] },
    }
    );

    ctx = document.getElementById('clears');
    var chart6 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["NP", "F", "AC", "EC", "NC", "HC", "EX", "FC"],
            datasets: [{
		    data:[lamppercent["NP"],lamppercent["F"],lamppercent["AC"],lamppercent["EC"],lamppercent["NC"],lamppercent["HC"],lamppercent["EX"],lamppercent["FC"]],
		    backgroundColor: ["#444","#400","#f0f","#0f0","#0ff","#f00","#fa0","#fcf"]
	    }]},
    }
    );
}
function drawStats(lamppercent, gradepercent, levellamppercent, levelgradepercent, levellamppercent_onlyplayed, levelgradepercent_onlyplayed){
    var p_np = {label:"NP", data:[], backgroundColor:"#444"};
    var p_flamp = {label:"F", data:[], backgroundColor:"#400"};
    var p_ac = {label:"AC", data:[], backgroundColor:"#f0f"};
    var p_ec = {label:"EC", data:[], backgroundColor:"#0f0"};
    var p_nc = {label:"NC", data:[], backgroundColor:"#0ff"};
    var p_hc = {label:"HC", data:[], backgroundColor:"#f00"};
    var p_ex = {label:"EX", data:[], backgroundColor:"#fa0"};
    var p_fc = {label:"FC", data:[], backgroundColor:"#fcf"};

    var gp_np = {label:"NP", data:[], backgroundColor:"#444"}
    var p_f = {label:"F", data:[], backgroundColor:"#400"}
    var p_e = {label:"E", data:[], backgroundColor:"#b00"}
    var p_d = {label:"D", data:[], backgroundColor:"#c55"}
    var p_c = {label:"C", data:[], backgroundColor:"#faa"}
    var p_b = {label:"B", data:[], backgroundColor:"#bbb"}
    var p_a = {label:"A", data:[], backgroundColor:"#fc8"}
    var p_aa = {label:"AA", data:[], backgroundColor:"#fa0"}
    var p_aaa = {label:"AAA", data:[], backgroundColor:"#ff0"}

    var op_p_flamp = {label:"F", data:[], backgroundColor:"#400"};
    var op_p_ac = {label:"AC", data:[], backgroundColor:"#f0f"};
    var op_p_ec = {label:"EC", data:[], backgroundColor:"#0f0"};
    var op_p_nc = {label:"NC", data:[], backgroundColor:"#0ff"};
    var op_p_hc = {label:"HC", data:[], backgroundColor:"#f00"};
    var op_p_ex = {label:"EX", data:[], backgroundColor:"#fa0"};
    var op_p_fc = {label:"FC", data:[], backgroundColor:"#fcf"};

    var op_p_f = {label:"F", data:[], backgroundColor:"#400"}
    var op_p_e = {label:"E", data:[], backgroundColor:"#b00"}
    var op_p_d = {label:"D", data:[], backgroundColor:"#c55"}
    var op_p_c = {label:"C", data:[], backgroundColor:"#faa"}
    var op_p_b = {label:"B", data:[], backgroundColor:"#bbb"}
    var op_p_a = {label:"A", data:[], backgroundColor:"#fc8"}
    var op_p_aa = {label:"AA", data:[], backgroundColor:"#fa0"}
    var op_p_aaa = {label:"AAA", data:[], backgroundColor:"#ff0"}

    for(var level = 1; level < 13; level++ ){

        p_np['data'].push(level in levellamppercent && "NP" in levellamppercent[level] ? levellamppercent[level]["NP"] : 0);
        p_flamp['data'].push(level in levellamppercent && "F" in levellamppercent[level] ? levellamppercent[level]["F"] : 0);
        p_ac['data'].push(level in levellamppercent && "AC" in levellamppercent[level] ? levellamppercent[level]["AC"] : 0);
        p_ec['data'].push(level in levellamppercent && "EC" in levellamppercent[level] ? levellamppercent[level]["EC"] : 0);
        p_nc['data'].push(level in levellamppercent && "NC" in levellamppercent[level] ? levellamppercent[level]["NC"] : 0);
        p_hc['data'].push(level in levellamppercent && "HC" in levellamppercent[level] ? levellamppercent[level]["HC"] : 0);
        p_ex['data'].push(level in levellamppercent && "EX" in levellamppercent[level] ? levellamppercent[level]["EX"] : 0);
        p_fc['data'].push(level in levellamppercent && "FC" in levellamppercent[level] ? levellamppercent[level]["FC"] : 0);

        gp_np['data'].push(level in levelgradepercent && "NP" in levelgradepercent[level] ? levelgradepercent[level]["NP"] : 0);
        p_f['data'].push(level in levelgradepercent && "F" in levelgradepercent[level] ? levelgradepercent[level]["F"] : 0);
        p_e['data'].push(level in levelgradepercent && "E" in levelgradepercent[level] ? levelgradepercent[level]["E"] : 0);
        p_d['data'].push(level in levelgradepercent && "D" in levelgradepercent[level] ? levelgradepercent[level]["D"] : 0);
        p_c['data'].push(level in levelgradepercent && "C" in levelgradepercent[level] ? levelgradepercent[level]["C"] : 0);
        p_b['data'].push(level in levelgradepercent && "B" in levelgradepercent[level] ? levelgradepercent[level]["B"] : 0);
        p_a['data'].push(level in levelgradepercent && "A" in levelgradepercent[level] ? levelgradepercent[level]["A"] : 0);
        p_aa['data'].push(level in levelgradepercent && "AA" in levelgradepercent[level] ? levelgradepercent[level]["AA"] : 0);
        p_aaa['data'].push(level in levelgradepercent && "AAA" in levelgradepercent[level] ? levelgradepercent[level]["AAA"] : 0);

        op_p_flamp['data'].push(level in levellamppercent_onlyplayed && "F" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["F"] : 0);
        op_p_ac['data'].push(level in levellamppercent_onlyplayed && "AC" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["AC"] : 0);
        op_p_ec['data'].push(level in levellamppercent_onlyplayed && "EC" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["EC"] : 0);
        op_p_nc['data'].push(level in levellamppercent_onlyplayed && "NC" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["NC"] : 0);
        op_p_hc['data'].push(level in levellamppercent_onlyplayed && "HC" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["HC"] : 0);
        op_p_ex['data'].push(level in levellamppercent_onlyplayed && "EX" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["EX"] : 0);
        op_p_fc['data'].push(level in levellamppercent_onlyplayed && "FC" in levellamppercent_onlyplayed[level] ? levellamppercent_onlyplayed[level]["FC"] : 0);

        op_p_f['data'].push(level in levelgradepercent_onlyplayed && "F" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["F"] : 0);
        op_p_e['data'].push(level in levelgradepercent_onlyplayed && "E" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["E"] : 0);
        op_p_d['data'].push(level in levelgradepercent_onlyplayed && "D" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["D"] : 0);
        op_p_c['data'].push(level in levelgradepercent_onlyplayed && "C" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["C"] : 0);
        op_p_b['data'].push(level in levelgradepercent_onlyplayed && "B" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["B"] : 0);
        op_p_a['data'].push(level in levelgradepercent_onlyplayed && "A" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["A"] : 0);
        op_p_aa['data'].push(level in levelgradepercent_onlyplayed && "AA" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["AA"] : 0);
        op_p_aaa['data'].push(level in levelgradepercent_onlyplayed && "AAA" in levelgradepercent_onlyplayed[level] ? levelgradepercent_onlyplayed[level]["AAA"] : 0);
    }


    var ctx = document.getElementById('lvlgrades_percent');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            datasets: [gp_np, p_f, p_e, p_d, p_c, p_b, p_a, p_aa, p_aaa] },
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

    ctx = document.getElementById('lvlclears_percent');
    var chart2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            datasets: [p_np, p_flamp, p_ac, p_ec, p_nc, p_hc, p_ex, p_fc] },
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

    ctx = document.getElementById('lvlgrades_percent_onlyplayed');
    var chart3 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            datasets: [op_p_f, op_p_e, op_p_d, op_p_c, op_p_b, op_p_a, op_p_aa, op_p_aaa] },
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

    ctx = document.getElementById('lvlclears_percent_onlyplayed');
    var chart4 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            datasets: [op_p_flamp, op_p_ac, op_p_ec, op_p_nc, op_p_hc, op_p_ex, op_p_fc] },
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
            labels: ["NP", "F", "E", "D", "C", "B", "A", "AA", "AAA"],
            datasets: [
		    {
			    data:[gradepercent["NP"],gradepercent["F"],gradepercent["E"],gradepercent["D"],gradepercent["C"],gradepercent["B"],gradepercent["A"],gradepercent["AA"],gradepercent["AAA"]],
			    backgroundColor: ["#444","#400","#b00","#c55","#faa","#bbb","#fc8","#fa0","#ff0"]
		    }] },
    }
    );

    ctx = document.getElementById('clears');
    var chart6 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["NP", "F", "AC", "EC", "NC", "HC", "EX", "FC"],
            datasets: [{
		    data:[lamppercent["NP"],lamppercent["F"],lamppercent["AC"],lamppercent["EC"],lamppercent["NC"],lamppercent["HC"],lamppercent["EX"],lamppercent["FC"]],
		    backgroundColor: ["#444","#400","#f0f","#0f0","#0ff","#f00","#fa0","#fcf"]
	    }]},
    }
    );

    ctx = document.getElementById('grades_onlyplayed');
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

    ctx = document.getElementById('clears_onlyplayed');
    var chart8 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["F", "AC", "EC", "NC", "HC", "EX", "FC"],
            datasets: [{
		    data:[lamppercent["F"],lamppercent["AC"],lamppercent["EC"],lamppercent["NC"],lamppercent["HC"],lamppercent["EX"],lamppercent["FC"]],
		    backgroundColor: ["#400","#f0f","#0f0","#0ff","#f00","#fa0","#fcf"]
	    }]},
    }
    );


}
