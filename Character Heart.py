import pygame, sys, random
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

size=(1000,700)
screen=pygame.display.set_mode(size)
clock= pygame.time.Clock()

Space=pygame.image.load("Fondo.jpg")


pygame.mouse.set_visible(0)
Heart=pygame.image.load("heart.png")
Heart.set_colorkey([255,255,255])

#coordenadas del corazon
coordx=10
coordy=10
#fps
speedx= 0
speedy= 0


coor_list=[]
for i in range(80):
    x =random.randint(0,1000)
    y= random.randint(0,700)
    coor_list.append([x,y])


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
     #Eventos que pasa con el teclado
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                speedx=-3
            if event.key==pygame.K_RIGHT:
                speedx= 3
            if event.key==pygame.K_UP:
                speedy=-5
            if event.key==pygame.K_DOWN:
                speedy= 5
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                speedx=0
            if event.key==pygame.K_RIGHT:
                speedx=0
            if event.key==pygame.K_UP:
                speedy=0
            if event.key==pygame.K_DOWN:
                speedy=0
    
           
            
    screen.blit(Space,[0,0])
    for coord in coor_list:
        pygame.draw.circle(screen,white, coord,2)
        coord[1]+=1
        if coord[1]>700:
            coord[1]=0
    coordx+=speedx
    coordy+=speedy
    
    
    screen.blit(Heart,[coordx,coordy])
    
    
    pygame.display.flip()
    clock.tick(60)