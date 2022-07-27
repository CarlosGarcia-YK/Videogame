"""Videogame made by Carlos G and Jair D"""



import pygame, sys, time, random
from tkinter import*
import serial, time

arduino = serial.Serial("COM6", 9600)

pygame.init()
#just colors 
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
#Classic variables 
screen = pygame.display.set_mode((1000, 900))
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

#Soundtrack Game
pygame.mixer.music.load("Soundtrack.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)

#Make the fondo and heart 
Space=pygame.image.load("Fondo.jpg")
pygame.mouse.set_visible(0)
Heart=pygame.image.load("heart.png")
#Soundtrack Game
pygame.mixer.music.load("Soundtrack.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)

#Heart´s coordenates 
coordx=100
coordy=450
#fps
speedx= 0
speedy= 0
speedN = -5
modegame = "NICE"
class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("enemey.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		
		if modegame == "EASY":
			self.rect.x -= 5
		if modegame == "NORMAL":
			self.rect.x -= 10
		if modegame == "HARD":
			self.rect.x -= 15
		if modegame == "TRYHARD":
			self.rect.x -= 25
		else:
			self.rect.x -=1
        
  

		if self.rect.x < 0:
			self.rect.x = +900
			self.rect.y = random.randrange(900)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("heart.png").convert()
		self.image.set_colorkey(white)
		self.rect = self.image.get_rect()

	def update(self):
		player.rect.x = coordx
		player.rect.y = coordy

run = True
timer =  0
realtime =0
press = "Press F to End"
Lifes = 5
vida = "Lifes"
#call the functions by a name 
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
player = Player()  
all_sprite_list.add(player)

Sound=pygame.mixer.Sound("Oof.mp3")
Sound.set_volume(0.7)
Final=pygame.mixer.Sound("Finally.mp3")
Final.set_volume(0.9)

for i in range(10): #How many enemies
	meteor = Meteor()
	meteor.rect.x = random.randrange(800,1300)
	meteor.rect.y = random.randrange(300,800)
	meteor_list.add(meteor)
	all_sprite_list.add(meteor)
while run:
        #timer 
        timer += 1
        clock.tick(120)
        all_sprite_list.update()
        
        #to make the conter
        if timer>120 :
            realtime+=1
            timer = 0
        #condition objects based in time
        if realtime< 15 and realtime>-1:
            
            modegame = "EASY"  
        if realtime >= 15 and realtime<30:
            
            
            modegame = "NORMAL"  
        if realtime >= 30 and realtime<50:
            
            modegame = "HARD"
        if realtime >= 50 and realtime<60:
            
            modegame = "TRYHARD"
        if realtime == 60 :
            meteor.rect.x = 440
            realtime = 61
            modegame = "YOU WON, FOR NOW"  
       #to restore the position every time 
        if realtime >=65:
            run = False
            
         #Movement when you want in keyboard 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            
             if event.key== pygame.K_LEFT:
                speedx=-25
             if event.key==pygame.K_RIGHT:
                speedx= 25
             if event.key==pygame.K_UP:
                speedy=-25
             if event.key==pygame.K_DOWN:
                speedy= 25
             if event.key == pygame.K_f: #Just if you want to fail 
                    modegame = "You have failed!"
                    realtime = 61
                    print("You has surrendered!")

        x = str(arduino.read().strip()).strip('b')
        #to move around in bottons 
        if x == "'1'":
            coordy = 700
        if x == "'2'":
            coordy= 200
        if x == "'3'":
            speedy= 10
        if x == "'4'":
            speedy= -10
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
        #The special movement 
        coordx+=speedx
        coordy+=speedy   
        
        meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
        for meteor in meteor_hit_list:
            if Lifes <= 0:
                print(realtime)
                realtime = 61
                modegame = "Game Over"
                print("F FOR YOU")
                run == False
            if Lifes ==0:
                Sound.set_volume(0.0)
                Final.play()
                pygame.mixer.music.set_volume(0.1)
                
                
        
            Lifes = Lifes -1
            print("You have failed !")
            Sound.play()
        #Close when the clock reach 65 seg
        #Print the objects 
        screen.blit(Space,[0,0])
        text = font.render(str(realtime),0,(200,60,80))
        end = font.render(str(press),0,(200,60,80))
        textcenter = font.render(str(modegame),0,(200,60,80))
        word = font.render(str(vida),0,(200,60,80))
        screen.blit(textcenter,(450,100))
        screen.blit(text, (850,100))
        screen.blit(end,(10,100))
        hearts = font.render(str(Lifes),0,(200,60,80))
        screen.blit(hearts,(200,100))
        screen.blit(word,(210,100))
        all_sprite_list.draw(screen)
        
        pygame.display.flip()



    
        

















    
           
            
    
    
    
   
    


        
        
    
