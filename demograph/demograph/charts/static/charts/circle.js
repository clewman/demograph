

    var html = '';
var red;
var green;
var blue;
var rgbColor;

function randomCol() {
  var randomColor = Math.floor(Math.random() * 256 );
  return randomColor;
}

function colors() {
red = randomCol();
green = randomCol();
blue = randomCol();
rgbColor = 'rgb(' + red + ',' + green + ',' + blue + ')';
html += '<div id="circle" style="background-color:' + rgbColor + '"></div>';
}

for (var i = 1; i <= 6; i += 1) {
    var divColors = colors();
}

document.write(html);

