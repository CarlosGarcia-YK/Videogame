"""Videogame made by Carlos G and Jair D"""

from hashlib import blake2b
from turtle import update
from typing_extensions import Self
import pygame, sys, time, random
from tkinter import*
import serial, time

#arduino = serial.Serial("COM6", 9600)

pygame.init()
#just colors 
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
#Classic variables 
screen = pygame.display.set_mode((1000, 900))
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

#Make the fondo and heart 
Space=pygame.image.load("Fondo.jpg")
pygame.mouse.set_visible(0)
Heart=pygame.image.load("heart.png")
Heart.set_colorkey([255,255,255])

#coordenadas del corazon
coordx=450
coordy=450
#fps
speedx= 0
speedy= 0




coor_list=[]
for i in range(80):
    x =random.randint(0,1000)
    y= random.randint(0,700)
    coor_list.append([x,y])

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("enemey.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x -= 10

		if self.rect.x < 0:
			self.rect.x = +900
			self.rect.y = random.randrange(100,800)



run = True
timer =  0
realtime =0
dt = 1
ap = 0
press = "Press F to End"
    
#call the functions by a name 
pikes = update

board = [0,10]
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(3):
	meteor = Meteor()
	meteor.rect.x = random.randrange(900)
	meteor.rect.y = random.randrange(600)

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)
    
while run:
        #timer 
        randomColor = random.randint(0,25)*10
        timer += dt
        clock.tick(60)
        all_sprite_list.update()
        
        #to make the conter
        if timer>60 :
            realtime+=1
            timer = 0
        #condition objects based in time
        if realtime< 15 and realtime>-1:
            screen.fill((0,0,0))
            modegame = "EASY"  
        if realtime >= 15 and realtime<30:
            meteor.rect.x -= 20
            screen.fill((0,0,0))
            modegame = "Normal"  
        if realtime >= 30 and realtime<50:
            meteor.rect.x -= 25
            screen.fill((ap,0,0))
            modegame = "HARD"
        if realtime >= 50 and realtime<60:
            meteor.rect.x -= 30
            screen.fill((ap,0,0))
            modegame = "TRYHARD"
        if realtime == 60 :
            meteor.rect.x = 450
            realtime = 61
            modegame = "YOU WON"  
       #to restore the position every time 
       
        
         
        
         
         
         #Movement when you want in keyboard 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            
             if event.key== pygame.K_LEFT:
                speedx=-20
             if event.key==pygame.K_RIGHT:
                speedx= 20
             if event.key==pygame.K_UP:
                speedy=-20
             if event.key==pygame.K_DOWN:
                speedy= 20
             if event.key == pygame.K_f: #Just if you want to fail 
                    modegame = "You have failed!"
                    realtime = 61
                    print("You has surrendered!")
        
            """
        x = str(arduino.read().strip()).strip('b')
        #to move around in bottons 
        if x == "'1'":
            speedx=-25
        if x == "'2'":
            speedx= 25
        if x == "'3'":
            speedy= 25
        if x == "'4'":
            speedy= -25
        if x == "'0'":
            speedy = 0
            speedx =0    
        
        #When the heart hit the boarders 
        if coordx >= 900:
            speedx = -10
        if coordx <= 0:
            speedx = 10
        if coordy <= 150:
            speedy = 10
        if coordy >= 750:
            speedy =-10
        """
        #The special movement 
        coordx+=speedx
        coordy+=speedy   
        
      
        
       
        #Close when the clock reach 65 seg
        if realtime >=65:
            run = False


                
         
        
    
         
        
        #Print the objects 
        screen.blit(Space,[0,0])
        
        text = font.render(str(realtime),0,(200,60,80))
        end = font.render(str(press),0,(200,60,80))
        textcenter = font.render(str(modegame),0,(200,60,80))
        screen.blit(textcenter,(450,100))
        screen.blit(text, (850,100))
        screen.blit(end,(10,100))
        all_sprite_list.draw(screen)
        screen.blit(Heart,[coordx,coordy])
        pygame.display.flip()



    
        
        

















    
           
            
    
    
    
   
    


        
        
    
