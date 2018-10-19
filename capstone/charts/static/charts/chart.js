

var lineDiv = document.getElementById('line-chart');

var traceA = {
    x:[2, 4, 5, 9, 34, 56],
    y:[2, 5, 7, 8, 32, 44],
    type: 'scatter'
};

var data = [traceA];

var layout = {
    title: 'Test Line Chart Plotly'
};

Plotly.plot( lineDiv, data, layout);