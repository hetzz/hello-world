let snake;
let rez=10; 
let food;
let col;
let row;
let height=400
let width=400
function setup() {
    createCanvas(width, height);
    line(200,200,width,height);
    frameRate(10);
    snake=new Snake();
    col=floor(width/rez);
    row=floor(height/rez);
    foodLocate();
  }
function foodLocate(){
    let x=floor(random(col));
    let y=floor(random(row));
    food=createVector(x,y);
}
function keyPressed()
{
    if(keyCode==LEFT_ARROW)
    {
    snake.setDir(-1,0);
    }
    else if(keyCode==RIGHT_ARROW)
    {
    snake.setDir(1,0);
    }
    else if(keyCode==DOWN_ARROW)
    {
    snake.setDir(0,1);
    }
    else if(keyCode==UP_ARROW)
    {
    snake.setDir(0,-1);
    }
}
  
  function draw() {
    scale(rez);
    background(0);
    snake.update();
    snake.show();
    if(snake.eat(food))
    {
        foodLocate();
    }
    if(snake.endGame())
    {
        print("End Game");
        background(179, 96, 115);
        noLoop();
        document.getElementById("result").innerHTML="END GAME..Refresh to start a new game";
    }
    noStroke();
    fill(179, 96, 115);
    rect(food.x,food.y,1,1);

  }
