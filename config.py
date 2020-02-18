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

if flag1 == 0 :
    winner= font2.render('Player 2 is the winner ',1, (255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(winner,(50,400))
    pygame.mixer.music.load('over.mp3')
    pygame.mixer.music.play()
    pygame.display.flip()
    pygame.time.delay(3000)
    thankyou=font2.render('Thanks for playing the game',1,(255,255,255))
    screen.blit(thankyou,(0,600))
    pygame.display.flip()
    pygame.time.delay(2000)
    done = True
if flag2 == 0 :
    winner= font2.render('Player 1 is the winner ',1, (255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(winner,(50,600))
    pygame.mixer.music.load('over.mp3')
    pygame.mixer.music.play()
    pygame.display.flip()
    pygame.time.delay(3000)
    thankyou=font2.render('Thanks for playing the game',1,(255,255,255))
    screen.blit(thankyou,(0,400))
    pygame.display.flip()
    pygame.time.delay(2000)
    done = True
    pygame.display.flip()
    pygame.display.update()
