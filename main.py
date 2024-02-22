import turtle
import random
import time
screen = turtle.Screen()
screen.tracer(0,0)
food = turtle.Turtle()
food.pu()
pressed_last=["right"]
length = 1
food.shape("circle")
food.color("blue")
food.speed(0)
gridturtle = turtle.Turtle()
gridturtle.speed(0)
foodpos = [0,0]
def drawgrid():
  for line in range(-300,300,20):
    gridturtle.pu()
    gridturtle.goto(300,line)
    gridturtle.pd()
    gridturtle.goto(-300,line)
  for line in range(-300,300,20):
    gridturtle.pu()
    gridturtle.goto(line,300)
    gridturtle.pd()
    gridturtle.goto(line,-300)
drawgrid()
def foodplacement():
  global foodpos
  x = random.randint(-15,14) * 20 + 10
  y = random.randint(-15,14) * 20 + 10
  foodpos[0] = x
  foodpos[1] = y
  food.goto(x,y)
  food.stamp()
for i in range(1):
  foodplacement()
snake = turtle.Turtle()
snake.pu()
snake.shape("square")
snake.color("purple")
snake.goto(10,10)
snake.speed(0)
gridturtle.ht()
snakepos = [(10,10)]
def grow():
  global snakepos
  global pressed_last
  global length
  x = snakepos[-1][0]
  y = snakepos[-1][1]
  if pressed_last[0] == "right":
    snakepos.append([x-20,y])
  if pressed_last[0] == "left":
    snakepos.append([x+20,y])
  if pressed_last[0] == "up":
    snakepos.append([x,y-20])
  if pressed_last[0] == "down":
    snakepos.append([x,y+20])
  length += 1
def check_food():
  global snakepos, foodpos
  if foodpos[0] == snakepos[0][0] and foodpos[1] == snakepos[0][1]:
    food.clear()
    grow()
    foodplacement()
def moveup():
  global pressed_last
  pressed_last.insert(0,"up")
  del pressed_last[length:]
def movedown():
  global pressed_last
  pressed_last.insert(0,"down")
  del pressed_last[length:]
def moveright():
  global pressed_last
  pressed_last.insert(0,"right")
  del pressed_last[length:]
def moveleft():
  global pressed_last
  pressed_last.insert(0,"left")
  del pressed_last[length:]
def drawsnake():
  global snake, snakepos
  snake.clear()
  for i in snakepos:
    snake.goto(i[0], i[1])
    snake.stamp()
  screen.update()
def move():
  global pressed_last, snakepos
  pressed_last.insert(0, pressed_last[0])
  del pressed_last[length:]
  temp1=snakepos[0][0]
  temp2=snakepos[0][1]
  if pressed_last[0] == "right":
    temp1 += 20
  if pressed_last[0] == "left":
    temp1 -= 20
  if pressed_last[0] == "up":
    temp2 += 20
  if pressed_last[0] == "down":
    temp2 -= 20
  snakepos.insert(0,(temp1,temp2))
  del snakepos[length:]
  time.sleep(0.1)
gameover= False
writing=turtle.Turtle()
writing.ht()
writing.pu()
writing.color("red")
def message():
  writing.write("You died! Score:" + str(length-1), align="center", font=("comic sans", 20))
  print("gameover")
  screen.update()
def check_gameover():
  global snakepos, gameover
  first = True
  for something in snakepos:
    if something[0] > 300:
      gameover = True
      message()
    if something[0] < -300:
      gameover = True
      message()
    if something[1] > 300:
      gameover = True
      message()
    if something[1] < -300:
      gameover = True
      message()  
    if not first:
      if snakepos[0] == something:
        gameover= True
        message()
    first = False
def loop():
  global gameover
  if not gameover:
    check_food()
    move()
    drawsnake()
    check_gameover()
    screen.ontimer(loop, 1)
loop()
screen.onkey(moveup, "Up")
screen.onkey(movedown, "Down")
screen.onkey(moveleft, "Left")
screen.onkey(moveright, "Right")
screen.listen()