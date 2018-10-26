// scatter and line plots. Change out "mode" for "lines" or "markers"
//change out 'type' for 'scatter' (line and scatter plots), 'bar' (bar graphs)
// can either have plotly menu bar always on, hidden until mouseover, or completely hidden. See bottom of page for other options
// see about doing an "if scatter: change marker size" to make scatter plots bigger but not anything else



let chart_type_ddl = document.querySelector('#chart_type_ddl')
chart_type_ddl.onchange = function () {
    let type = chart_type_ddl.options[chart_type_ddl.selectedIndex].value
    let mode = chart_type_ddl.options[chart_type_ddl.selectedIndex].title
    myFunction(type, mode)
}


function myFunction(type, mode) {

    if (type === 'choropleth') {


    Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv', function (err, rows) {
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
        Plotly.plot(finalGraph, data, layout, {showLink: false});
    });

}
    else if (type == 'bar' || type == 'line' || type == 'scatter') {
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
            title: 'Title',
            showlegend: true
        };
    }

    else if (type == 'pie') { //pie
        var data = [{
            values: [19, 26, 55],
            labels: ['Residential', 'Non-Residential', 'Utility'],
            type: type
        }];
    }



    Plotly.newPlot('finalGraph', data, layout, {displayModeBar: false});

}




// to make it editable with plotly on their site, always shows
// var layout = {
//     title: 'Always Display the Modebar',
//     showlegend: false};
// Plotly.newPlot('myDiv', data, layout, {displayModeBar: true});

