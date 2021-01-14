#Caitlyn Stone-Whitehead
#CSCI 101 - C
#References: https://www.youtube.com/watch?v=whErCLh0-QU
#Create Project
#Time: 12hrs

from tkinter import *

import random

import time

tk = Tk()

tk.title("BRICK BREAKER")

tk.resizable(0,0)

tk.wm_attributes("-topmost",1)

score = 0

canvas = Canvas(tk, bg = "black",width = 500, height = 500, bd = 0, highlightthickness = 0)

canvas.pack()

tk.update()

colors = ["Red","Orange","Yellow","Green","Blue","Purple","White","Pink","Gold","Salmon","Indian Red","SteelBlue1","PaleGreen1","cyan","deep pink"]


class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id,250,150)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        start = [-3,-2,-1,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        random.shuffle(start)
        self.y = start[1]

    def hitpaddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False

    def hitbrick1(self,pos):
        self.brick1 = brick1
        brick_pos = self.canvas.coords(self.brick1.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        
    def hitbrick2(self,pos):
        self.brick2 = brick2
        brick_pos = self.canvas.coords(self.brick2.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick3(self,pos):
        self.brick3 = brick3
        brick_pos = self.canvas.coords(self.brick3.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick4(self,pos):
        self.brick4 = brick4
        brick_pos = self.canvas.coords(self.brick4.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick5(self,pos):
        self.brick5 = brick5
        brick_pos = self.canvas.coords(self.brick5.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick6(self,pos):
        self.brick6 = brick6
        brick_pos = self.canvas.coords(self.brick6.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        
    def hitbrick7(self,pos):
        self.brick7 = brick7
        brick_pos = self.canvas.coords(self.brick7.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick8(self,pos):
        self.brick8 = brick8
        brick_pos = self.canvas.coords(self.brick8.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick9(self,pos):
        self.brick9 = brick9
        brick_pos = self.canvas.coords(self.brick9.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick10(self,pos):
        self.brick10 = brick10
        brick_pos = self.canvas.coords(self.brick10.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        
    def hitbrick11(self,pos):
        self.brick11 = brick11
        brick_pos = self.canvas.coords(self.brick11.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        
    def hitbrick12(self,pos):
        self.brick12 = brick12
        brick_pos = self.canvas.coords(self.brick12.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick13(self,pos):
        self.brick13 = brick13
        brick_pos = self.canvas.coords(self.brick13.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick14(self,pos):
        self.brick14 = brick14
        brick_pos = self.canvas.coords(self.brick14.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick15(self,pos):
        self.brick15 = brick15
        brick_pos = self.canvas.coords(self.brick15.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick16(self,pos):
        self.brick16 = brick16
        brick_pos = self.canvas.coords(self.brick16.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
    
        
    def hitbrick17(self,pos):
        self.brick17 = brick17
        brick_pos = self.canvas.coords(self.brick17.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        

    def hitbrick18(self,pos):
        self.brick18 = brick18
        brick_pos = self.canvas.coords(self.brick18.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
    

    def hitbrick19(self,pos):
        self.brick19 = brick19
        brick_pos = self.canvas.coords(self.brick19.id)
        if brick_pos == []:
            return False
        exit
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False

    def hitbrick20(self,pos):
        self.brick20 = brick20
        brick_pos = self.canvas.coords(self.brick20.id)
        if brick_pos == []:
            return False
        exit
        
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        

        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = - self.y
        if pos[0] <= 0:
            self.x = -self.x
        if pos[3] >= self.canvas_height:
            self.y = - self.y
        if pos[2] >= self.canvas_width:
            self.x = -self.x
        if self.hitpaddle(pos) == True:
            self.y = -self.y
        if self.hitbrick1(pos) == True:
            self.y = -self.y
        if self.hitbrick2(pos) == True:
            self.y = -self.y
        if self.hitbrick3(pos) == True:
            self.y = -self.y
        if self.hitbrick4(pos) == True:
            self.y = -self.y
        if self.hitbrick5(pos) == True:
            self.y = -self.y
        if self.hitbrick6(pos) == True:
            self.y = -self.y
        if self.hitbrick7(pos) == True:
            self.y = -self.y
        if self.hitbrick8(pos) == True:
            self.y = -self.y
        if self.hitbrick9(pos) == True:
            self.y = -self.y
        if self.hitbrick10(pos) == True:
            self.y = -self.y
        if self.hitbrick11(pos) == True:
            self.y = -self.y
        if self.hitbrick12(pos) == True:
            self.y = -self.y
        if self.hitbrick13(pos) == True:
            self.y = -self.y
        if self.hitbrick14(pos) == True:
            self.y = -self.y
        if self.hitbrick15(pos) == True:
            self.y = -self.y
        if self.hitbrick16(pos) == True:
            self.y = -self.y
        if self.hitbrick17(pos) == True:
            self.y = -self.y
        if self.hitbrick18(pos) == True:
            self.y = -self.y
        if self.hitbrick19(pos) == True:
            self.y = -self.y
        if self.hitbrick20(pos) == True:
            self.y = -self.y
        if pos[3] >= 430:
            self.y = 0
            self.x = 0
            GameOver(canvas)
            Score(canvas)
            
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<Left>',self.turn_left)
        self.canvas.bind_all('<Right>',self.turn_right)
        

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
    
    def turn_left(self,evt):
        self.x = -2
        
    def turn_right(self,evt):
        self.x = 2

class Brick1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,50,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 49 >= ball_pos[0] and 0 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)
class Brick2:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(50,0,100,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 99 >= ball_pos[0] and 50 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick3:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(100,0,150,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 149 >= ball_pos[0] and 100 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick4:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(150,0,200,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 199 >= ball_pos[0] and 150 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick5:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(200,0,250,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 249 >= ball_pos[0] and 200 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick6:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(250,0,300,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 299 >= ball_pos[0] and 250 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick7:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(300,0,350,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 349 >= ball_pos[0] and 300 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick8:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(350,0,400,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 399 >= ball_pos[0] and 350 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick9:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(400,0,450,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 449 >= ball_pos[0] and 400 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick10:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(450,0,500,20, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 499 >= ball_pos[0] and 450 <= ball_pos[2]:
            if 20 >= ball_pos[1] and 0 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick11:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,20,50,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 49 >= ball_pos[0] and 0 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick12:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(50,20,100,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 99 >= ball_pos[0] and 50 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick13:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(100,20,150,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 149 >= ball_pos[0] and 100 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)
class Brick14:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(150,20,200,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 199 >= ball_pos[0] and 150 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)
class Brick15:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(200,20,250,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 249 >= ball_pos[0] and 200 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)
class Brick16:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(250,20,300,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 299 >= ball_pos[0] and 250 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick17:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(300,20,350,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 349 >= ball_pos[0] and 300 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick18:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(350,20,400,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 399 >= ball_pos[0] and 350 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)
class Brick19:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(400,20,450,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 449 >= ball_pos[0] and 400 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class Brick20:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(450,20,500,40, fill = color)
    def destroy(self):
        global score
        self.ball = ball
        ball_pos = self.canvas.coords(self.ball.id)
        if 500 >= ball_pos[0] and 450 <= ball_pos[2]:
            if 40 >= ball_pos[1] and 20 <= ball_pos[3]:
                score +=1000
                canvas.delete(self.id)

class GameOver:
    def __init__(self,canvas):
        self.canvas = canvas
        self.id = canvas.create_text(250,250,text= "GAME OVER", font= ("Times",30),fill="white")

class Score:
    def __init__(self,canvas):
        self.canvas = canvas
        self.id = canvas.create_text(450,450,text= f"SCORE: {score}", font= ("Times",10),fill="white")
        
random.shuffle(colors)
paddle = Paddle(canvas, colors[0])
random.shuffle(colors)
ball = Ball(canvas, paddle, colors[0])
random.shuffle(colors)
brick1 = Brick1(canvas,colors[0])

random.shuffle(colors)
brick2 = Brick2(canvas,colors[0])

random.shuffle(colors)
brick3 = Brick3(canvas,colors[0])

random.shuffle(colors)
brick4 = Brick4(canvas,colors[0])

random.shuffle(colors)
brick5 = Brick5(canvas,colors[0])

random.shuffle(colors)
brick6 = Brick6(canvas,colors[0])

random.shuffle(colors)
brick7 = Brick7(canvas,colors[0])

random.shuffle(colors)
brick8 = Brick8(canvas,colors[0])

random.shuffle(colors)
brick9 = Brick9(canvas,colors[0])

random.shuffle(colors)
brick10 = Brick10(canvas,colors[0])

random.shuffle(colors)
brick11 = Brick11(canvas,colors[0])

random.shuffle(colors)
brick12 = Brick12(canvas,colors[0])

random.shuffle(colors)
brick13 = Brick13(canvas,colors[0])

random.shuffle(colors)
brick14 = Brick14(canvas,colors[0])

random.shuffle(colors)
brick15 = Brick15(canvas,colors[0])

random.shuffle(colors)
brick16 = Brick16(canvas,colors[0])

random.shuffle(colors)
brick17 = Brick17(canvas,colors[0])

random.shuffle(colors)
brick18 = Brick18(canvas,colors[0])

random.shuffle(colors)
brick19 = Brick19(canvas,colors[0])

random.shuffle(colors)
brick20 = Brick20(canvas,colors[0])


while 1:
    ball.draw()
    paddle.draw()
    brick20.destroy()
    brick19.destroy()
    brick18.destroy()
    brick17.destroy()
    brick16.destroy()
    brick15.destroy()
    brick14.destroy()
    brick13.destroy()
    brick12.destroy()
    brick11.destroy()
    brick10.destroy()
    brick9.destroy()
    brick8.destroy()
    brick7.destroy()
    brick6.destroy()
    brick5.destroy()
    brick4.destroy()
    brick3.destroy()
    brick2.destroy()
    brick1.destroy()
    tk.update_idletasks()
    tk.update()
    time.sleep(.01)


    
