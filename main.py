import turtle

wn = turtle.Screen()
wn.title("Pong by Om")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#batl
bat_l = turtle.Turtle()
bat_l.speed(0)
bat_l.shape("square")
bat_l.color("white")
bat_l.shapesize(stretch_len=1, stretch_wid=5)
bat_l.penup()
bat_l.goto(-350, 0)


#batr
bat_r = turtle.Turtle()
bat_r.speed(1)
bat_r.shape("square")
bat_r.color("white")
bat_r.shapesize(stretch_len=1, stretch_wid=5)
bat_r.penup()
bat_r.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx=0.5
ball.dy=0.5


#line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=300, stretch_len=0.1)
line.penup()
line.goto(0, 0)


#vline
vline = turtle.Turtle()
vline.speed(0)
vline.shape("square")
vline.color("white")
vline.shapesize(stretch_len=400, stretch_wid=0.1)
vline.penup()
vline.goto(0, 250)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Calibri", 24, "normal"))

#score
score_a = 0
score_b = 0


#Function
def bat_l_up():
    y = bat_l.ycor()
    y += 20
    bat_l.sety(y)

def bat_l_down():
    y = bat_l.ycor()
    y -= 20
    bat_l.sety(y)

def bat_r_up():
    y = bat_r.ycor()
    y += 20
    bat_r.sety(y)

def bat_r_down():
    y = bat_r.ycor()
    y -= 20
    bat_r.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(bat_l_up, "w")
wn.onkeypress(bat_l_down, "s")
wn.onkeypress(bat_r_up, "Up")
wn.onkeypress(bat_r_down, "Down")


#main ganme loop
while True:
    wn.update()

    #move the ballz
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #border
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Calibri", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Calibri", 24, "normal"))

    #collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < bat_r.ycor()+ 50 and ball.ycor() > bat_r.ycor() -50):
        ball.setx(330)
        ball.dx *= -1
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < bat_l.ycor() + 50 and ball.ycor() > bat_l.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1









