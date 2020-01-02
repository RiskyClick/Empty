import turtle

wn = turtle.Screen()
wn.title("The Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0



#paddle A
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.penup()
a.goto(-350, 0)
a.shapesize(stretch_wid=5, stretch_len=1)


#paddle B
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.penup()
b.goto(350, 0)
b.shapesize(stretch_wid=5, stretch_len=1)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = -.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center", font= ("Courier", 24, "normal"))


#Functions
def a_up():
    y = a.ycor()
    y += 20
    a.sety(y)

def a_down():
    y = a.ycor()
    y -= 20
    a.sety(y)

def b_up():
    y = b.ycor()
    y += 20
    b.sety(y)

def b_down():
    y = b.ycor()
    y -= 20
    b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(a_down, "s")
wn.onkeypress(a_up, "w")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")




while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddel ball collitions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < b.ycor() + 50 and ball.ycor() > b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() < -350 and ball.ycor() < a.ycor() + 50 and ball.ycor() > a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1