import pygame
import math
from random import randint,choice

pygame.init()
screen=pygame.display.set_mode((900,545))
pygame.display.set_caption('T E N N I S')

background=pygame.image.load('Court.png')  
player1Img=pygame.image.load('Racket.png')
player1X=20
player1Y=250
player1_speed=0

player2Img=pygame.image.load('Racket.png')
player2X=825
player2Y=250
player2_speed=0

ballImg=pygame.image.load('ball.png')
ballX=10
ballY=10
ball_speed=0
ballY_speed=0
ball_state='off'

def speed():
	global ball_speed
	ball_speed=10

def c_on():
	global ball_state
	ball_state='on'

def c_off():
	global ball_state
	ball_state='off'

def ball(x,y):
	screen.blit(ballImg,(x+30,y+45))

def player1(x,y):
	screen.blit(player1Img,(x,y))

def player2(x,y):
	screen.blit(player2Img,(x,y))

def iscollision1(ballX,ballY,player1X,player1Y):
	D=math.sqrt((math.pow(ballX-player1X,2)) + (math.pow(ballY-player1Y,2)))
	
	if D<75:
		return True
	else:
		return False

def iscollision2(ballX,ballY,player2X,player2Y):
	D=math.sqrt((math.pow(ballX-player2X,2)) + (math.pow(ballY-player2Y,2)))

	if D<75:
		return True
	else:
		return False

left_score = 0
right_score = 0

left_win = False
right_win = False

l=[-5,5,-4,4,-6,6]

running=True
while running:
	screen.fill((200,200,200))
	screen.blit(background,(0,0))
	player1(player1X,player1Y)
	player2(player2X,player2Y)
	left_font = pygame.font.SysFont(None,70)
	left_img = left_font.render(str(left_score)+' :',True,(0,0,0))

	right_font = pygame.font.SysFont(None,70)
	right_img = right_font.render(str(right_score),True,(0,0,0))

	screen.blit(left_img,(400,11))
	screen.blit(right_img,(475,11))
	#ball(player1X,player1Y)
	collision1=iscollision1(ballX,ballY,player1X,player1Y)
	collision2=iscollision2(ballX,ballY,player2X,player2Y)


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

	if event.type==pygame.KEYDOWN:
		if event.key==pygame.K_DOWN:
			player2_speed=17
		if event.key==pygame.K_UP:
			player2_speed=-17
		
		if event.key==pygame.K_s:
			player1_speed=17
		if event.key==pygame.K_w:
			player1_speed=-17


		#Starting of the game
		if ball_state == 'off':
			if left_win==False and right_win==False and event.key==pygame.K_SPACE:
				ballY=player1Y
				ballX=player1X
				ball(ballX,ballY)
				ball_speed=22
				c_on()

			if right_win == True and event.key==pygame.K_SPACE:
				# right_score+=1
				ballY=player1Y
				ballX=player1X
				ball(ballX,ballY)
				# ball_speed=22
				c_on()
				right_win=False
			
			if left_win == True and event.key==pygame.K_SPACE:
				# left_score+=1
				ballY=player2Y
				ballX=player2X
				ball(ballX,ballY)
				# ball_speed=-22
				c_on()
				left_win = False


	#effect of taking your hands off
	if event.type==pygame.KEYUP:
		if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
			player2_speed=0

		if event.key==pygame.K_w or event.key==pygame.K_s:
			player1_speed=0


	#Speed and movement
	player2Y+=player2_speed
	player1Y+=player1_speed
	ball(ballX,ballY)

	ballX+=ball_speed
	ballY+=ballY_speed

	if ball_state == 'on':
		if collision2:
			ballY_speed=choice(l)
			ball_speed=-(randint(25,30))
			

	if ball_state == 'on':
		if collision1:
			ballY_speed=choice(l)
			ball_speed=randint(25,30)
			


	#hot to reset the game when lost
	if ballX>=850:
		left_win = True
		ballX =800
		ballY =30
		ball_speed=0
		left_score+=1
		ballY_speed=0
		c_off()

	if ballX<=0:
		right_win = True
		ballX =30
		ballY =30
		ball_speed=0
		ballY_speed=0
		right_score+=1
		c_off()



	#Boudaries
	if player1Y<=45:
		player1Y=45
	if player1Y>=470:
		player1Y=470

	if player2Y<=45:
		player2Y=45
	if player2Y>=470:
		player2Y=470

	# BallY boundaries
	if ballY<=40:
		ballY=40
	if ballY>=415:
		ballY=415

#Shoot the ball to a random Xpath of x end

	pygame.display.update()
	pygame.display.update()

	pygame.display.update()
