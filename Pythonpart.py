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

def obstacles():
    
   random_pos = random.randint(20,55)*10
   obstacles_places = [950,random_pos]
   return obstacles_places
def obstacles2():
    random_pos2 = random.randint(60,75)*10
    obstacles_places2 = [950,random_pos2]
    return obstacles_places2
def obstacles3():
    random_pos3  = random.randint(20,75)*10
    obstacles_places3 = [1050,random_pos3]
    return obstacles_places3


run = True
timer =  0
realtime =0
dt = 1
ap = 0
press = "Press F to End"
    
#call the functions by a name 
pikes = obstacles()
pikes2 = obstacles2()
pikes3 = obstacles3()
board = [0,10]
    
while run:
        #timer 
        randomColor = random.randint(0,25)*10
        timer += dt
        clock.tick(60)
        
        
        #to make the conter
        if timer>60 :
            realtime+=1
            timer = 0
        #condition objects based in time
        if realtime< 15 and realtime>-1:
            pikes[0] -= 10
            pikes2[0] -= 10
            pikes3[0] -= 15
            screen.fill((0,0,0))
            modegame = "EASY"  
        
        if realtime >= 15 and realtime<30:
            pikes[0] -= 15
            pikes2[0] -= 15
            pikes3[0] -= 20
            screen.fill((0,0,0))
            modegame = "Normal"  
        
        if realtime >= 30 and realtime<50:
            pikes[0] -=20
            pikes2[0] -=20
            pikes3[0] -=30
            
            screen.fill((ap,0,0))
            
            modegame = "HARD"
        if realtime >= 50 and realtime<60:
            pikes[0] -=35
            pikes2[0] -=35
            pikes3[0] -=40
            
            screen.fill((ap,0,0))
            
            modegame = "TRYHARD"
        if realtime == 60 :
            
            pikes[0] = 450
            pikes2[0] = 450
            pikes3[0] = 450
            realtime = 61
            modegame = "YOU WON"  
       #to restore the position every time 
        if pikes[0] <= 0:
            pikes = obstacles()
        if pikes2[0] <= 0:
            pikes2 = obstacles2()
        if pikes3[0]<=0:
            pikes3 = obstacles3()
        
         
        
         
         
         #Movement when you want in keyboard 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            
             if event.key== pygame.K_LEFT:
                speedx=-50
             if event.key==pygame.K_RIGHT:
                speedx= 50
             if event.key==pygame.K_UP:
                speedy=-50
             if event.key==pygame.K_DOWN:
                speedy= 50
             if event.key == pygame.K_f: #Just if you want to fail 
                    modegame = "You have failed!"
                    realtime = 61
                    print("You has surrendered!")
        
            
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
        
        #The special movement 
        coordx+=speedx
        coordy+=speedy   
        
      
        
       
        #Close when the clock reach 65 seg
        if realtime >=65:
            run = False


                
         
        
    
         
        
        #Print the objects 
        screen.blit(Space,[0,0])
        pygame.draw.rect(screen,(50,22,22), pygame.Rect(board[0],board[1], 1000,150))
        pygame.draw.rect(screen,(randomColor,255,255), pygame.Rect(pikes[0], pikes[1], 200, 75))
        pygame.draw.rect(screen,(255,randomColor,255), pygame.Rect(pikes2[0], pikes2[1], 100, 50))
        pygame.draw.rect(screen,(255,255,randomColor), pygame.Rect(pikes3[0], pikes3[1], 100, 25))
        text = font.render(str(realtime),0,(200,60,80))
        end = font.render(str(press),0,(200,60,80))
        textcenter = font.render(str(modegame),0,(200,60,80))
        screen.blit(textcenter,(450,100))
        screen.blit(text, (850,100))
        screen.blit(end,(10,100))
        
        screen.blit(Heart,[coordx,coordy])
        pygame.display.flip()



    
        
        

















    
           
            
    
    
    
   
    


        
        
    
