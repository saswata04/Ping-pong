''' A Simple Ping Pong game made using Python Turtle  module. Enjoy! '''
import turtle
import winsound

# Player Names
player_a = input("Enter Player A's name : ")# Enter player names
player_b = input("Enter Player B's name : ")# Enter player names

# window config
wn = turtle.Screen()# creates a window object
wn.title('>>PING PONG<<')# window title
wn.bgcolor('black')# window background color
wn.setup(width=800, height=600)# window dimensions(width & height)
wn.tracer(2,0)# if uncomment --> change the ball.dx and ball.dy also

# Score
score_a = 0
score_b = 0

# Net
net = turtle.Turtle()# creates a net object
net.speed(0)# animation speed
net.color('white')# net color
net.penup()
net.goto(0, -300)# set net position
net.pendown()
net.left(90)
net.forward(600)
net.hideturtle()# hides the turtle head

# Paddle A config
paddle_a = turtle.Turtle()# creates a Turtle object
paddle_a.speed(0)# animation speed # It's not the paddle speed
paddle_a.shape('square')# paddle shape # By default the size is 20px by 20px
paddle_a.color('white')# paddle color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)# resize the turtle's dimensions # by default the turtle faces towards right
paddle_a.penup()
paddle_a.goto(-350, 0)# set paddle position

# Paddle B config
paddle_b = turtle.Turtle()# creates a Turtle object
paddle_b.speed(0)# animation speed # It's not the paddle speed
paddle_b.shape('square')# paddle shape # By default the size is 20px by 20px
paddle_b.color('white')# paddle color
paddle_b.shapesize(stretch_wid=5, stretch_len=1)# resize the turtle's dimensions # by default the turtle faces towards right
paddle_b.penup()
paddle_b.goto(350, 0)# set paddle position

# Ball config
ball = turtle.Turtle()# creates a Turtle object
ball.speed(0)# animation speed # It's not the ball speed
ball.shape('circle')# ball shape # By default the size is 20px by 20px
ball.color('white')# ball color
ball.penup()
ball.goto(0, 0)# set ball position
ball.dx = 0.4# change in x coordinate of ball
ball.dy = 0.4# change in y coordinate of ball

# Pen config
pen = turtle.Turtle()# creates a Turtle object
pen.speed(0)# animation speed
pen.color('grey')# pen color
pen.penup()
pen.hideturtle()# hides the turtle head
pen.goto(0, 260)# set pen position
pen.write(f'{player_a} : 0     {player_b} : 0', align='center', font=('Courier', 24, 'italic'))# to write something on the window using the pen object

# Functions
def paddle_a_up():
    y = paddle_a.ycor()# getting the current y coordinate of paddle
    y += 20# adding 20px bcz y upwards is +ve
    paddle_a.sety(y)# setting the y coordinate of paddle

def paddle_a_down():
    y = paddle_a.ycor()# getting the current y coordinate of paddle
    y -= 20# substracting 20px bcz y downwards is -ve
    paddle_a.sety(y)# setting the y coordinate of paddle

def paddle_b_up():
    y = paddle_b.ycor()# getting the current y coordinate of paddle
    y += 20# adding 20px bcz y upwards is +ve
    paddle_b.sety(y)# setting the y coordinate of paddle

def paddle_b_down():
    y = paddle_b.ycor()# getting the current y coordinate of paddle
    y -= 20# substracting 20px bcz y downwards is -ve
    paddle_b.sety(y)# setting the y coordinate of paddle

# Key Binding
wn.listen()# asking the window to take input from keybord
wn.onkeypress(paddle_a_up, 'w')# binds key 'w'(lowercase/capslock off) with paddle_a_up() i.e. when we press 'w' paddle_a_up() executes
wn.onkeypress(paddle_a_down, 's')# binds key 's'(lowercase/capslock off) with paddle_a_down() i.e. when we press 's' paddle_a_down() executes
wn.onkeypress(paddle_b_up, 'Up')# binds key 'Up'(lowercase/capslock off) with paddle_b_up() i.e. when we press 'Up' paddle_b_up() executes
wn.onkeypress(paddle_b_down, 'Down')# binds key 'Down'(lowercase/capslock off) with paddle_b_down() i.e. when we press 'Down' paddle_b_down() executes

# Main game loop
while True:
    wn.update()# updates the window everytime the loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)# setting x coordinate(setx) of the ball by getting the current x coordinate(xcor) and adding change in x coordinate(dx) to it
    ball.sety(ball.ycor() + ball.dy)# setting y coordinate(sety) of the ball by getting the current y coordinate(ycor) and adding change in y coordinate(dy) to it

    # Border Checking
    # top border
    if ball.ycor() > 290:# if current y coordinate of the ball becomes > 290
        ball.sety(290)# set the y coordinate of the ball to 290
        ball.dy *= -1# reverse the direction of change in y
        winsound.PlaySound('pong.wav', winsound.SND_ASYNC)# enter border & ball collision sound

    # bot border
    if ball.ycor() < -290:# if current y coordinate of the ball becomes < -290
        ball.sety(-290)# set the y coordinate of the ball to -290
        ball.dy *= -1# reverse the direction of change in y
        winsound.PlaySound('pong.wav', winsound.SND_ASYNC)# enter border & ball collision sound
    
    # right border
    if ball.xcor() > 390:# if current x coordinate of the ball becomes > 390
        ball.goto(0, 0)# set ball position 
        ball.dx *= -1# reverse the direction of change in x
        score_a += 1# increment Player A score
        # if score_a%5 == 0 or score_b%5 == 0:
        #     ball.dx += 0.1
        #     ball.dy += 0.1
        pen.clear()# clears whatever was written by the pen object previously
        pen.write(f'{player_a} : {score_a}     {player_b} : {score_b}', align='center', font=('Courier', 24, 'italic'))# to write something on the window using the pen object
        winsound.PlaySound('exit.wav', winsound.SND_ASYNC)# enter border & ball collision sound

    # left border
    if ball.xcor() < -390:# if current x coordinate of the ball becomes < -390
        ball.goto(0, 0)# set ball position 
        ball.dx *= -1# reverse the direction of change in x
        score_b += 1# increment Player B score
        # if score_a%5 == 0 or score_b%5 == 0:
        #     ball.dx += 0.1
        #     ball.dy += 0.1
        pen.clear()# clears whatever was written by the pen object previously
        pen.write(f'{player_a} : {score_a}     {player_b} : {score_b}', align='center', font=('Courier', 24, 'italic'))# to write something on the window using the pen object
        winsound.PlaySound('exit.wav', winsound.SND_ASYNC)# enter border & ball collision sound
    
    # Paddle and Ball Collisions
    # paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):# if x coordinate of ball is > and < left face of paddle_b and y coordinate of the ball is < and > top and bot of paddle_b
        ball.setx(340)# set x coordinate of the ball to 340(left face of paddle_b)
        ball.dx *= -1# reverse the direction of change in x
        winsound.PlaySound('paddle.wav', winsound.SND_ASYNC)# enter paddle & ball collision sound

    # paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):# if x coordinate of ball is > and < right face of paddle_a and y coordinate of the ball is < and > top and bot of paddle_a
        ball.setx(-340)# set x coordinate of the ball to -340(right face of paddle_b)
        ball.dx *= -1# reverse the direction of change in x
        winsound.PlaySound('paddle.wav', winsound.SND_ASYNC)# enter paddle & ball collision sound