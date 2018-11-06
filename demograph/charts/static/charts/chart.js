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

        Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv', function(err, rows){
      function unpack(rows, key) {
          return rows.map(function(row) { return row[key]; });
      }

 var data = [{
              type: 'choropleth',
              locationmode: 'USA-states',
              locations: unpack(rows, 'code'),
              z: unpack(rows, 'total exports'),
              text: unpack(rows, 'state'),
              zmin: 0,
              zmax: 17000,
              colorscale: [
                [0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
                [0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
                [0.8, 'rgb(117,107,177)'], [1, 'rgb(84,39,143)']
              ],
            colorbar: {
              title: 'Millions USD',
              thickness: 0.2
            },
            marker: {
              line:{
                color: 'rgb(255,255,255)',
                width: 2
              }
            }
          }];

console.log(data.locations);
  var layout = {
          title: '2011 US Agriculture Exports by State',
          geo:{
            scope: 'usa',
            showlakes: true,
            lakecolor: 'rgb(255,255,255)'
          }
      };
      Plotly.plot(finalGraph, data, layout, {showLink: false});
  });

}
    else if (type == 'bar' || type == 'line' || type == 'scatter') {
        trace1 = {
            type: type,
            x: x, //x is gender
            y: y, //y is income level
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

    else if (type == 'pie') { //pie
        var data = [{
            values: [19, 26, 55],
            labels: ['Residential', 'Non-Residential', 'Utility'],
            type: type
        }];
    }



    Plotly.newPlot('finalGraph', data, layout, {displayModeBar: false});

}



