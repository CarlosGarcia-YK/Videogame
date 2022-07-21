"""Videogame made by Carlos G and Jair D"""
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
    
    random_pos = random.randint(10,50)*10
    obstacles_places = [900,random_pos]
    return obstacles_places
def obstacles2():
    
    
    random_pos2 = random.randint(60,85)*10
    obstacles_places2 = [950,random_pos2]
    return obstacles_places2
def obstacles3():
    random_pos3 = random.randint(10,85)*10
    obstacles_places3 = [1050,random_pos3]
    return obstacles_places3
def game():
    run = True
    timer =  0
    realtime =0
    dt = 1
    
    
    pikes = obstacles()
    pikes2 = obstacles2()
    pikes3 = obstacles3()
    while run:
        #timer 
        timer += dt
        clock.tick(10)
        if timer>10 :
            realtime+=1
            timer = 0
        #condition objects 
        if realtime < 15 :
            pikes[0] -= 50
            pikes2[0] -= 50
            pikes3[0] -= 70
            modegame = "EASY"  
        if realtime>15:
            pikes[0] -=100
            pikes2[0] -=100
            pikes3[0] -=100
            modegame = "HARD"
        if realtime >16:
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
        
         
         
        
    
         
        screen.fill((0,0,0))
        
        #Print the objects 
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(pikes[0], pikes[1], 100, 50))
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(pikes2[0], pikes2[1], 100, 50))
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(pikes3[0], pikes3[1], 100, 50))
        text = font.render(str(realtime),0,(200,60,80))
        textcenter = font.render(str(modegame),0,(200,60,80))
        screen.blit(textcenter,(450,120))
        screen.blit(text, (850,120))
        
        
        pygame.display.flip()
game()

pygame.quit()
    
        
        
    
