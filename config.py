import pygame,sys
from pygame.locals import *
import time
import random
pygame.init()
screen = pygame.display.set_mode((950,1050))

image=pygame.image.load("2.jpg")
image=pygame.transform.scale(image,(50,100))
blue=pygame.image.load("blue.png")
blue=pygame.transform.scale(blue,(60,100))
pink=pygame.image.load("pink.png")
pink=pygame.transform.scale(pink,(60,100))
yellow=pygame.image.load("yellow.png")
yellow=pygame.transform.scale(yellow,(60,100))
ship=pygame.image.load("white.jpeg")
ship=pygame.transform.scale(ship,(60,100))
green = pygame.image.load("green.png")
green = pygame.transform.scale(green,(50,100))
green2= pygame.image.load("green2.png")
green2= pygame.transform.scale(green2,(50,100))
font = pygame.font.SysFont('comicsans',50,True)
font2=pygame.font.SysFont('comicsans',100,True)
bg=pygame.image.load("2.jpg")
bg=pygame.transform.scale(bg,(950,1050))


done = False
is_blue = True
x = 0
y = 0
x_2=0
y_2=850
velocity = 3
score1 = 0
score2=0
count = 1
flag2 = 3
flag1 = 3
level=1
i=0
j=0
t1=0
t2=0
pscore1=0
pscore2=0
answer=0
player1=0
player2=0

'''
y1=0
y4=155
y6=305
y2=455
y5=605
y3=755

def moveit(i):
        global y1
        global y2
        global y3
        global y4
        global y5
        global y6
        y1 += i
        if y1 < 900:
            position = pygame.Rect(75,y1,60,100)
        else :
            y1 = 0
            position = pygame.Rect(75,y1,60,100)
        screen.blit(ship,position)

        y2 += i
        if y2 < 900:
            position = pygame.Rect(150+75,y2,60,100)
        else :
            y2 = 0
            position = pygame.Rect(150+75,y2,60,100)
        screen.blit(ship,position)
        
        y3 += i
        if y3 < 900:
            position = pygame.Rect(300+75,y3,60,100)
        else :
            y3 = 0
            position = pygame.Rect(300+75,y3,60,100)
        screen.blit(ship,position)
        
        y4 += i
        if y4 < 900:
            position = pygame.Rect(450+75,y4,60,100)
        else :
            y4 = 0
            position = pygame.Rect(450+75,y4,60,100)
        screen.blit(ship,position)
        
        y5 += i
        if y5 < 900:
            position = pygame.Rect(600+75,y5,60,100)
        else :
            y5 = 0
            position = pygame.Rect(600+75,y5,60,100)
        screen.blit(ship,position)
        
        y6 += i
        if y6 < 900:
            position = pygame.Rect(750+75,y6,60,100)
        else :
            y6 = 0
            position = pygame.Rect(750+75,y6,60,100)
        screen.blit(ship,position)
        '''
pressed = pygame.key.get_pressed()
def press():
        global x
        global y
        global score1
        global pscore1
        if pressed[pygame.K_UP] and y > 2: 
                y -= 3
        if pressed[pygame.K_DOWN] and y < 897 -50: 
                y += 3
        if pressed[pygame.K_LEFT] and x > 2: 
                x -= 3
                score1-=1
        if pressed[pygame.K_RIGHT] and x < 898: 
                x += 3
                score1+=1
        if score1 == 50 :
                pscore1 += 15
                score1 = 0
def press2():
        global x_2
        global y_2
        global score2
        global pscore2
        if pressed[pygame.K_UP] and y_2 > 2: 
                y_2 -= 3
        if pressed[pygame.K_DOWN] and y_2 < 897 -50: 
                y_2 += 3
        if pressed[pygame.K_LEFT] and x_2 > 2: 
                x_2 -= 3
                score2-=1
        if pressed[pygame.K_RIGHT] and x_2 < 898: 
                x_2 += 3
                score2+=1
        if score2 == 50 :
                pscore2 +=15
                score2 = 0