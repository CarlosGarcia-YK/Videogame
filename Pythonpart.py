"""Videogame made by Carlos G and Jair D"""
from typing import Counter
import pygame, sys, time, random
from os import system
from tkinter import*
import serial, time

#arduino = serial.Serial("COM6", 9600)

pygame.init()

screen = pygame.display.set_mode((700, 700))
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

def obstacles():
    random_pos = random.randint(0,49)*10
    obstacles_places = [490,random_pos]
    return obstacles_places

def game():
    run = True
    timer =  0
    dt = 1
    
    pikes = obstacles()
    while run:
        
        timer += dt
        clock.tick(1)
        if timer == 60:
         timer = 0
         
        screen.fill((0,0,0))
        text = font.render(str(timer),0,(200,60,80))
        screen.blit(text, (480,20))
        
        
        pygame.display.flip()
game()

pygame.quit()
    
        
        
    
