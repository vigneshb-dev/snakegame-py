import turtle as t
import time as ti
import random as r
class snake:
    def __init__(self):
        self.segments=[]
        self.positions=[(0,0),(-12,0),(-24,0)]
        for x in self.positions:
            self.add_segment(x)
    def add_segment(self,position):
        path=t.Turtle("square")
        path.color("white")
        path.penup()
        path.goto(position)
        self.segments.append(path)
    def movement(self):
        for x in range(len(self.segments)-1,0,-1):
            new_x=self.segments[x-1].xcor()
            new_y=self.segments[x-1].ycor()
            self.segments[x].goto(new_x,new_y)
        self.segments[0].forward(12)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def left(self):
        self.segments[0].left(90)
    def right(self):
        self.segments[0].right(90)
class food:
    def __init__(self):
        self.food=t.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.shapesize(0.6,0.6)
        self.food.penup()
        self.refresh()
    def refresh(self):
        self.food.goto(r.randint(-350,350),r.randint(-350,350))
        self.food.speed("fastest")
class score:
    def __init__(self):
        self.score=0
        self.score_text=t.Turtle()
        self.score_text.hideturtle()
        self.score_text.penup()
        self.score_text.goto(0,320)
        self.score_text.color("white")
        self.score_text.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
    def update_score(self):
        self.score+=1
        self.score_text.clear()
        self.score_text.color("white")
        self.score_text.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
class collision:
    def __init__(self):
        self.collision=t.Turtle()
        self.collision.hideturtle()
        self.collision.penup()
        self.collision.goto(0,0)
    def game_over(self):
        self.collision.color("white")
        self.collision.write("Game Over",align="center",font=("Arial",24,"normal"))
screen=t.Screen()
screen.setup(width=750,height=750)
screen.bgcolor("black")
screen.title("2D Snake Game")
screen.tracer(0)
Snake=snake()
Food=food()
Score=score()
Collision=collision()
running=True
while running:
    screen.update()
    ti.sleep(0.1)
    t.listen()
    Snake.movement()
    t.onkey(Snake.left,"Left")
    t.onkey(Snake.right,"Right")
    if Snake.segments[0].distance(Food.food)<12:
        Food.refresh()
        Score.update_score()
        Snake.extend()
    if abs(Snake.segments[0].xcor())>350 or abs(Snake.segments[0].ycor())>350:
        Collision.game_over()
        screen.update()
        running=False
    for segment in Snake.segments[1:]:
        if Snake.segments[0].distance(segment)<12:
            Collision.game_over()
            screen.update()
            running=False
screen.exitonclick()
