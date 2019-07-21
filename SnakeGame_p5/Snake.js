class Snake{
    constructor()
    {
        this.body=[];
        this.body[0]=createVector(0,1);
        this.xd=1;
        this.yd=0;
        this.len=1;
    }
    setDir(x,y)
    {
        this.xd=x;
        this.yd=y;
    }
    update()
    {
        let top=this.body[this.body.length-1].copy();
        this.body.shift();
        top.x+=this.xd;
        top.y+=this.yd;
        this.body.push(top);
    }
    expand()
    {
        let top=this.body[this.body.length-1].copy();
        this.len++;
        this.body.push(top);
    }
    eat(pos)
    {
        let top=this.body[this.body.length-1].copy();
        let x=top.x;
        let y=top.y;
        if(x==pos.x && y==pos.y)
        {
            this.expand();
            return true;
        }
        return false;
    }
    
  endGame() {
    let x = this.body[this.body.length-1].x;
    let y = this.body[this.body.length-1].y;
    if(x > col-1 || x < 0 || y > row-1 || y < 0) 
    {
        return true;
    }
    for(let i = 0; i < this.body.length-2; i++) 
        {
            let part = this.body[i];
            if(part.x == x && part.y == y) 
            {
                return true;
            }
        }
        return false;
    }

    show()
    {
        for(let i=0;i<this.body.length;i++)
        {
            document.getElementById("score").innerHTML=this.body.length;
            fill(104, 243, 233);
            noStroke();
            rect(this.body[i].x,this.body[i].y,1,1);
        }
    }
}