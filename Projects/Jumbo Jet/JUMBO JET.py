import pygame
from random import randint
import math

pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption('JUMBO JET')

icon=pygame.image.load('Spaceship.png')

pygame.display.set_icon(icon)

background=pygame.image.load('SKY.png')


planeImg=pygame.image.load("jet-plane.png")
planeY=236
planeX=20
planeX_change=0
planeY_change=0


enemyImg=pygame.image.load("plane(1).png")
enemyX=750
enemyY=randint(0,200)
enemyY_change=0
enemyX_change=randint(10,25)

enemy2Img=pygame.image.load("plane(1).png")
enemy2X=750
enemy2Y=randint(200,400)
enemy2X_change=randint(10,25)

enemy3Img=pygame.image.load("plane(1).png")
enemy3X=750
enemy3Y=randint(400,600)
enemy3X_change=randint(10,25)


bulletImg=pygame.image.load('bull.png')
bullX=0
bullY=0
bullX_change=17
bull_state='off'

score=0

def plane(x,y):
    screen.blit(planeImg,(x,y))

o=(randint(100,300))
p=(randint(400,500))


def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def enemy2(x,y):
    screen.blit(enemy2Img,(x,y))

def enemy3(x,y):
    screen.blit(enemy3Img,(x,y))
    
def bull(x,y):
    screen.blit(bulletImg,(x+40,y+20))
    
def change_state():
    global bull_state
    bull_state='on'
    
#The value for bullX and bullY changes so i renamed it as bullet for i can change it in the while loop
def iscollision1(bulletX,bulletY,enemyX,enemyY):
    distance=math.sqrt((math.pow(bulletX-enemyX,2)) + (math.pow(bulletY-enemyY,2)))
    if distance<40:
        return True
    else:
        False
        
    
def iscollision2(bulletX,bulletY,enemy2X,enemy2Y):
    distance=math.sqrt((math.pow(bulletX-enemy2X,2)) + (math.pow(bulletY-enemy2Y,2)))
    if distance<40:
        return True
    else:
        False


def iscollision3(bulletX,bulletY,enemy3X,enemy3Y):
    distance=math.sqrt((math.pow(bulletX-enemy3X,2)) + (math.pow(bulletY-enemy3Y,2)))
    if distance<40:
        return True
    else:
        False

def dodge1(planeX,planeY,enemyX,enemyY):
    distance=math.sqrt((math.pow(planeX-enemyX,2)) + (math.pow(planeY-enemyY,2)))
    if distance>50:
        return True
    else:
        return False

def dodge2(planeX,planeY,enemy2X,enemy2Y):
    distance=math.sqrt((math.pow(planeX-enemy2X,2)) + (math.pow(planeY-enemy2Y,2)))
    if distance>50:
        return True
    else:
        return False

def dodge3(planeX,planeY,enemy3X,enemy3Y):
    distance=math.sqrt((math.pow(plane3X-enemyX,2)) + (math.pow(plane3Y-enemyY,2)))
    if distance>50:
        return True
    else:
        return False

score_value=0
font1=pygame.font.Font('freesansbold.ttf',20)
textX=10
textY=10

def show_score(x,y):
    score=font1.render('Hit: '+ str(score_value),True,(0,0,0)) 
    screen.blit(score,(x,y))

    
running=True
while running:

    screen.fill((200,200,0))
    screen.blit(background,(0,0))
    plane(planeX,planeY)
    enemy(enemyX,enemyY)
    enemy2(enemy2X,enemy2Y)
    enemy3(enemy3X,enemy3Y)

    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            planeX_change=12
        if event.key==pygame.K_LEFT:
            planeX_change=-12
        if event.key==pygame.K_UP:
            planeY_change=-12
        if event.key==pygame.K_DOWN:
            planeY_change=12
        if event.key==pygame.K_x:
            if bull_state == 'off':
                bullX=planeX
                bullY=planeY
                bull(bullX,bullY)
                bullX_change=25
                #change state to on
                change_state()
            

    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
            planeX_change=0
        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            planeY_change=0
            
           
    
    
    #Movement
    planeX+=planeX_change
    planeY+=planeY_change
    enemyX+=-enemyX_change
    enemy2X+=-enemy2X_change
    enemy3X+=-enemy3X_change


    #Respawn
    if enemyX<=0:
        enemyY=randint(0,40)
        enemyX_change=randint(15,30)
        enemyX=750
        
    if enemy2X<=0:
        enemy2Y=randint(100,300)
        enemy2X_change=randint(15,30)
        enemy2X=750
        
    if enemy3X<=0:
        enemy3Y=randint(400,500)
        enemy3X_change=randint(15,30)
        enemy3X=750
        
        
    #If i shoot
    if bull_state == 'on':
        bull(bullX,bullY)
        bullX+=bullX_change

    #If i miss
    if bullX>=800:
        bullX=planeX
        bull_state='off'
       
    
    #BOUNDARIES for my jet
    if planeX<=20:
        planeX=20
    if planeX>=700:
        planeX=700
    if planeY<=0:
        planeY=0
    if planeY>=536:
        planeY=536


    show_score(textX,textY)

    #Collision
    collision1=iscollision1(bullX,bullY,enemyX,enemyY)
    collision2=iscollision2(bullX,bullY,enemy2X,enemy2Y)
    collision3=iscollision3(bullX,bullY,enemy3X,enemy3Y)
    if collision1:
        global bullet_state
        score_value+=1
        #return bullet
        bullX=planeX
        bullY=planeY
        #change bullet state
        bull_state='off'
        #return the enemy
        enemyX=800
        #variate the speed
        enemyX_change=randint(10,25)
        
        

    if collision2:
        global bullet_state
        score_value+=1
        #return bullet
        bullX=planeX
        bullY=planeY
        #change bullet state
        bull_state='off'
        #return enemy
        enemy2X=800
        #variate speed
        enemy2X_change=randint(10,25)
        

    if collision3:
        global bullet_state
        score_value+=1
        #return bullet
        bullX=planeX
        bullY=planeY
        #change bullet state
        bull_state='off'
        #retrun enemy
        enemy3X=800
        #variate speed
        enemy3X_change=randint(10,25)



    swerve1=dodge1(planeX,planeY,enemyX,enemyY)
    if swerve1:
        pass
    if not swerve1:
        pass


    
    pygame.display.update()



    




    pygame.display.update()
