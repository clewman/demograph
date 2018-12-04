
// scatter and line plots. Change out "mode" for "lines" or "markers"
//change out 'type' for 'scatter' (line and scatter plots), 'bar' (bar graphs)
// can either have plotly menu bar always on, hidden until mouseover, or completely hidden. See bottom of page for other options
// see about doing an "if scatter: change marker size" to make scatter plots bigger but not anything else


let chart_type_ddl = document.querySelector('#chart_type_ddl')
chart_type_ddl.onchange = function () {
    let type = chart_type_ddl.options[chart_type_ddl.selectedIndex].value
    let mode = chart_type_ddl.options[chart_type_ddl.selectedIndex].title
    let a = []
    myFunction(type, mode, a)
}


// need to set x and y
function myFunction(type, mode, a) {

     if (type == 'bar' || type == 'line' || type == 'scatter') {

        trace1 = {
            type: type,
            x: x,
            y: y,
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
            x: x,
            y: y,
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

    else if (type == 'pie') {
        var data = [{
            values: a,
            labels: ['Residential', 'Non-Residential', 'Utility'],
            type: type
        }];
    }
    Plotly.newPlot('finalGraph', data, layout, {displayModeBar: false});
}



