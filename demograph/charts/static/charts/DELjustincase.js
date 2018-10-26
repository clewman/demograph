
//
// let graph_div_names = ['scatter_div', 'pie_div', 'choropleth_div']
// let graph_divs = []
// for (let i=0; i<graph_div_names.length; ++i) {
//     let graph_div = document.createElement('div')
//     graph_div.id = graph_div_names[i]
//     // add it to the dom
//     graph_div.appendChild(graph_divs)
//
// }
//
// // on click
// for (let i=0; i<graph_divs.length; ++i) {
//     graph_divs[i].style.display = 'none'
// }
// document.querySelector('#'+type).style.display = ''
//


let chart_type_ddl = document.querySelector('#chart_type_ddl')
chart_type_ddl.onchange = function () {
    // document.querySelector('#finalGraph').innerHTML = '';
    // document.querySelector('#finalGraph').className = '';
    let type = chart_type_ddl.options[chart_type_ddl.selectedIndex].value
    let mode = chart_type_ddl.options[chart_type_ddl.selectedIndex].title
    myFunction(type, mode)

}


function myFunction(type, mode) {
    if (type === 'bar' || type === 'line' || type === 'scatter') {

        trace1 = {
            type: type,
            x: [1, 2, 3, 4],
            y: [10, 15, 13, 17],
            mode: mode,
            name: 'Red',
            line: {
                color: 'rgb(219, 64, 82)',
                width: 3
            },
            marker: {size: 12}
        };

        trace2 = {
            type: type,
            x: [1, 2, 3, 4],
            y: [12, 9, 15, 12],
            mode: mode,
            name: 'Blue',
            line: {
                color: 'rgb(66, 244, 89)',
                width: 1
            },
            marker: {size: 12}
        };

        var data = [trace1, trace2];

        var layout = {
            title: 'Hide the Modebar',
            showlegend: true
        };
        Plotly.newPlot('finalGraph', data, layout, {displayModeBar: false});
    } else if (type === 'pie') { //pie
        var data = [{
            values: [19, 26, 55],
            labels: ['Residential', 'Non-Residential', 'Utility'],
            type: type
        }];
    }
    } else { //choropleth
        let data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv'
        Plotly.d3.csv(data_url, function (err, rows) {
            function unpack(rows, key) {
                return rows.map(function (row) {
                    return row[key];
                });
            }

            console.log(unpack(rows, 'postal'));
            var data = [{
                type: 'choropleth',
                locationmode: 'country names',
                locations: unpack(rows, 'location'),
                z: unpack(rows, 'alcohol'),
                text: unpack(rows, 'location'),
                autocolorscale: true
            }];

            var layout = {
                title: 'Pure alcohol consumption<br>among adults (age 15+) in 2010',
                geo: {
                    projection: {
                        type: 'robinson'
                    }
                }
            };
            Plotly.plot('finalGraph', data, layout, {showLink: false});
        });
    }


}

