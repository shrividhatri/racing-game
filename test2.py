import pygame,sys
from pygame.locals import *
import time
import random
from config import *
#+++++++++++++++++++++++++++++++++++++++++++++#
pygame.init()
screen = pygame.display.set_mode((950,1050))
pygame.display.set_caption('CAR OBSTRACLES GAME')
#+++++++++++++++++++++++++++++++++++++++++++++#
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
green2= pygame.image.load("greend.png")
green2= pygame.transform.scale(green2,(50,100))
font = pygame.font.SysFont('comicsans',50,True)
font2=pygame.font.SysFont('comicsans',100,True)
bg=pygame.image.load("2.jpg")
bg=pygame.transform.scale(bg,(950,1050))
#+++++++++++++++++++++++++++++++++++++++++++++#
pygame.mixer.music.load('game.mp3')
pygame.mixer.music.play(-1)
#+++++++++++++++++++++++++++++++++++++++++++++#
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
#+++++++++++++++++++++++++++++++++++++++++++++#
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

#+++++++++++++++++++++++++++++++++++++++++++++#
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
#+++++++++++++++++++++++++++++++++++++++++++++#
def collision1():
        global count
        global x
        global y
        global flag1
        if x > 0-50 and x < 0+50 :
                if y < 200+100 and y > 200-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 450-50 and x < 450+50 :
                if y < 600+100 and y > 600-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 300-50 and x < 300+50 :
                if y < 50+100 and y > 50-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 150-50 and x < 150+50 :
                if y < 700+100 and y > 700-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(ptext,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 750-50 and x < 750+50 :
                if y < 350+100 and y > 350-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 600-50 and x < 600+50 :
                if y < 75+100 and y > 75-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 900-50 and x < 900+50 :
                if y < 125+100 and y > 125-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        #--------------------#
        if x > 75-50 and x < 75+50 :
                if y < y1+100 and y > y1-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 150+75-50 and x < 150+75+50 :
                if y < y2+100 and y > y2-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 375-50 and x < 375+50 :
                if y < y3+100 and y > y3-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 525-50 and x < 525+50 :
                if y < y4+100 and y > y4-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 675-50 and x < 675+50 :
                if y < y5+100 and y > y5-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
        if x > 825-50 and x < 825+50 :
                if y < y6+100 and y > y6-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 2
                        x=0
                        y=0
                        flag1 -=1
#+++++++++++++++++++++++++++++++++++++++++++++#

def collision2():
        global count
        global x_2
        global y_2
        global flag2
        if x_2 > 0-50 and x_2 < 0+50 :
                if y_2 < 200+100 and y_2 > 200-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 450-50 and x_2 < 450+50 :
                if y_2 < 600+100 and y_2 > 600-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 300-50 and x_2 < 300+50 :
                if y_2 < 50+100 and y_2 > 50-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=0
                        flag2 -= 1
        if x_2 > 150-50 and x_2 < 150+50 :
                if y_2 < 700+100 and y_2 > 700-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 750-50 and x_2 < 750+50 :
                if y_2 < 350+100 and y_2 > 350-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 600-50 and x_2 < 600+50 :
                if y_2 < 75+100 and y_2 > 75-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 900-50 and x_2 < 900+50 :
                if y_2 < 125+100 and y_2 > 125-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        #--------------------#
        if x_2 > 75-50 and x_2 < 75+50 :
                if y_2 < y1+100 and y_2 > y1-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 150+75-50 and x_2 < 150+75+50 :
                if y_2 < y2+100 and y_2 > y2-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 375-50 and x_2 < 375+50 :
                if y_2 < y3+100 and y_2 > y3-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 525-50 and x_2 < 525+50 :
                if y_2 < y4+100 and y_2 > y4-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 675-50 and x_2 < 675+50 :
                if y_2 < y5+100 and y_2 > y5-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
        if x_2 > 825-50 and x_2 < 825+50 :
                if y_2 < y6+100 and y_2 > y6-100 :
                        text = font.render('COLLIDED',0,(0,0,0))
                        screen.blit(text,(500,955))
                        count = 1
                        x_2=0
                        y_2=850
                        flag2 -= 1
#+++++++++++++++++++++++++++++++++++++++++++++#
clock = pygame.time.Clock()
screen.blit(bg,(0,0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                
        pressed = pygame.key.get_pressed()
        if count == 1 :
                i+=1
                t1=i/40
                press()
        if count == 2 :
                press2()
                j+=1
                t2=j/40
             
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0),
        pygame.draw.rect(screen,(255,165,0),(0,0,60,950))
        pygame.draw.rect(screen,(255,165,0),(150,0,60,950))
        pygame.draw.rect(screen,(255,165,0),(300,0,60,950))
        pygame.draw.rect(screen,(255,165,0),(450,0,60,950))
        pygame.draw.rect(screen,(255,165,0),(600,0,60,950))
        pygame.draw.rect(screen,(255,165,0),(750,0,60,950))
        pygame.draw.rect(screen,(255,165,0),(900,0,60,950))
        pygame.draw.rect(screen,(255,000,0),(0,0,50,100))
        pygame.draw.rect(screen,(255,000,0),(900,850,50,100))
        pygame.draw.rect(screen,color,(0,850,50,100))
        pygame.draw.rect(screen,color,(900,0,60,100))
        #pygame.draw.rect(screen, color, pygame.Rect(x_2,y_2,50,100))
        position2 = pygame.Rect(x_2,y_2,50,100)
        position = pygame.Rect(x,y,50,100)
        screen.blit(green,position)
        screen.blit(green2,position2)
        screen.blit(blue,(0,200))
        screen.blit(blue,(450,600))
        screen.blit(pink,(300,50))
        screen.blit(pink,(150,700))
        screen.blit(pink,(750,350))
        screen.blit(yellow,(600,75))
        screen.blit(yellow,(900,125))
        winner= font.render('draw ',1, (255,255,255))
        answer = 0
        player1 = pscore1 - t1
        player2 = pscore2 - t2
        if player1 < player2 :
                answer = 2
        if player1 > player2 :
                answer = 1
        if player1 == player2 :
                winner= font2.render('Draw ',1, (255,255,255))
        if x >= 897 and y >= 846 :
            x=0
            y=0
            if pscore1 == 165 :
                pscore1 = 180
            if pscore1 == 75 :
                pscore1 = 90
            count = 2
        if x_2 >= 897 and y_2 <=2 :
            x_2=0
            y_2=850
            count = 1
            if pscore2 == 165 :
                pscore2 = 180
            if pscore2 == 75 :
                pscore2 = 90
            level +=1
            winner= font2.render('Player ' + str(answer) + ' is the winner',1, (255,255,255))
            winner2= font2.render(' of Level' + str (level),1, (255,255,255))
            screen.blit(bg,(0,0))
            screen.blit(winner,(70,400))
            screen.blit(winner2,(220,600))
            pygame.display.flip()
            pygame.time.delay(3000)
        moveit(velocity)
        pygame.draw.rect(screen,(0,255,40),(0,950,950,100))
        font = pygame.font.SysFont('comicsans',50,True)
        text = font.render('P1Score:' + str(pscore1) ,1,(0,0,0))
        text2= font.render('P2Score:' + str(pscore2),1,(0,0,0))
        start1=font.render('Start1' , 1,(255,255,255))
        start2=font.render('Start2' , 1,(255,255,255))
        end1=font.render('End1' , 1,(255,255,255))
        end2=font.render('End2' , 1,(255,255,255))
        levell=font.render('Level:' + str(level) ,1,(255,0,0))
        timer1 = font.render('Timer1:' + str(t1) ,1,(0,0,255))
        timer2 = font.render('Timer2:' + str(t2) ,1,(0,0,255))
        screen.blit(levell,(410,970))
        screen.blit(timer1,(240,970))
        screen.blit(timer2,(540,970))
        screen.blit(text,(30,970))
        screen.blit(text2,(720,970))
        screen.blit(start1,(0,0))
        screen.blit(start2,(0,900))
        screen.blit(end1,(860,900))
        screen.blit(end2,(860,0))
        collision1()
        collision2()
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
        clock.tick(60)