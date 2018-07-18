var target;
var startPos;
var diam; // diameter of target
var rocket;

var gridscale = 10;

function setup() {
  createCanvas(800,720);
  diam = 40;
  startPos = createVector(20,20,0);
  rocket = new Rocket(startPos, startPos);
}

function draw() {
  background(220);

  // target
  ellipse(mouseX, mouseY, diam, diam)
  target = createVector(mouseX, mouseY);
  rocket.target = target;
  rocket.run();
}




