"""Videogame made by Carlos G and Jair D"""
from turtle import delay
from typing import Counter
import pygame, sys, time, random
from os import system
from tkinter import*
import serial, time

#arduino = serial.Serial("COM6", 9600)

pygame.init()

screen = pygame.display.set_mode((900, 900))
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

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
def game():
    run = True
    timer =  0
    realtime =0
    dt = 1
    ap = 0
    press = "Press F to End"
    
    
    pikes = obstacles()
    pikes2 = obstacles2()
    pikes3 = obstacles3()
    board = [0,10]
    
    while run:
        #timer 
        randomColor = random.randint(0,25)*10
        timer += dt
        clock.tick(10)
        
        if timer>10 :
            realtime+=1
            timer = 0
        #condition objects 
        if realtime < 15 and realtime>-1:
            pikes[0] -= 50
            pikes2[0] -= 50
            pikes3[0] -= 70
            screen.fill((0,0,0))
            modegame = "EASY"  
        if realtime >= 15 and realtime<30:
            pikes[0] -=100
            pikes2[0] -=100
            pikes3[0] -=100
            ap += 1
            screen.fill((ap,0,0))
            
            modegame = "HARD"
        if realtime == 30 :
            pikes[0] = 450
            pikes2[0] = 450
            pikes3[0] = 450
            realtime = 30
            modegame = "YOU WON"  
        if pikes[0] <= 0:
            pikes = obstacles()
        if pikes2[0] <= 0:
            pikes2 = obstacles2()
        if pikes3[0]<=0:
            pikes3 = obstacles3()
        
         
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    modegame = "You have failed!"
                    realtime = 31
                    print("You has surrendered!")
        
        if realtime >=35:
                run = False
                     
                    


                
         
        
    
         
        
        #Print the objects 
        pygame.draw.rect(screen,(50,22,22), pygame.Rect(board[0],board[1], 1000,150))
        pygame.draw.rect(screen,(randomColor,255,255), pygame.Rect(pikes[0], pikes[1], 100, 25))
        pygame.draw.rect(screen,(255,randomColor,255), pygame.Rect(pikes2[0], pikes2[1], 100, 25))
        pygame.draw.rect(screen,(255,255,randomColor), pygame.Rect(pikes3[0], pikes3[1], 100, 25))
        text = font.render(str(realtime),0,(200,60,80))
        end = font.render(str(press),0,(200,60,80))
        textcenter = font.render(str(modegame),0,(200,60,80))
        screen.blit(textcenter,(450,100))
        screen.blit(text, (850,100))
        screen.blit(end,(10,100))
        
        
        pygame.display.flip()
game()


    
        
        
    
