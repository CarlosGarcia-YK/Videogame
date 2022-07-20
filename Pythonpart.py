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
    
    random_pos = random.randint(10,85)*10
    obstacles_places = [890,random_pos]
    return obstacles_places

def game():
    run = True
    timer =  0
    dt = 1
    
    pikes = obstacles()
    while run:
        
        timer += dt
        clock.tick(10)
        
        if timer < 15 :
            pikes[0] -= 100
        if timer>15:
            pikes[0] -=200
        if pikes[0] <= 0:
            pikes = obstacles()
        
        if timer == 60:
         timer = 0
         
        
    
         
        screen.fill((0,0,0))
        text = font.render(str(timer),0,(200,60,80))
        
        pygame.draw.rect(screen,(255,255,255), pygame.Rect(pikes[0], pikes[1], 200, 50))
        screen.blit(text, (850,120))
        
        
        pygame.display.flip()
game()

pygame.quit()
    
        
        
    
