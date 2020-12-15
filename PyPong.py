import turtle

Gamewindow = turtle.Screen()
Gamewindow.title("PyPong")
Gamewindow.bgcolor('black')
Gamewindow.setup(width=800, height=600)
Gamewindow.tracer(0)

# Paddles
left_paddle = turtle.Turtle()
left_paddle.speed(0) #max speed
left_paddle.shape("square")
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0) #max speed
right_paddle.shape("square")
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #max speed
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.25  
ball.dy = 0.25

# Score Title
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('white')
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0 , 260)
scoreboard.write('Player 1: 0   Player 2: 0' , align='center', font=('Courier', 24, 'normal'))

# Score
score_a = 0
score_b = 0

#Functions
# Paddle A Up/Down
def left_paddle_up():
    y= left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y= left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Paddle B Up/Down
def right_paddle_up():
    y= right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y= right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

#Keyboard Bindings
Gamewindow.listen()
Gamewindow.onkeypress(left_paddle_up, "w")
Gamewindow.onkeypress(left_paddle_down, "s")
Gamewindow.onkeypress(right_paddle_up, "Up")
Gamewindow.onkeypress(right_paddle_down, "Down")

# Main Game
while True:
    Gamewindow.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top Boundary
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Bottom Boundary
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # Left Boundary
    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_a += 1
        scoreboard.clear()
        scoreboard.write('Player 1: {}   Player 2: {}'.format(score_a, score_b) , align='center', font=('Courier', 24, 'normal'))
    # Right Boundary
    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write('Player 1: {}   Player 2: {}'.format(score_a, score_b) , align='center', font=('Courier', 24, 'normal'))

# Collisions
    # Left Paddle Collision
    if ball.xcor() < -340 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1 
    #Right Paddle Collision
    elif ball.xcor() > 340 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1
    