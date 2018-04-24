
var targetPos = pVector();
var startPos;
var diam; // diameter of target

function setup() {
  createCanvas(1240,720);
}

function draw() {
  background(220);


  ellipse(mouseX, mouseY, 40, 40)
  targetPos = pVector(mouseX, mouseY);
}
