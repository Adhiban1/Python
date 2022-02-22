import pygame
import numpy as np
from math import sin, cos, pi
import random

pygame.init()
#1920, 1080
sx, sy = 1920, 1080
size = (sx, sy)
screen = pygame.display.set_mode(size)
done = False
color = (0,255,0)
a = 0
r1 = 350
r = r1 - 5
speed = 2
m = random.choice(np.linspace(0,355,10))
cx, cy = sx/2, sy/2
center = (cx, cy)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((0,0,0))
    
    pressed = pygame.key.get_pressed()
    a += 0.01*speed
    if pressed[pygame.K_LEFT]:
        a -= 0.01*2*speed
    if a>=2*pi:
        a = 0
    
    
    for i in np.linspace(0, 0.225, 100):
        
        if a>(m-15)*2*pi/360 and a<(m+15)*2*pi/360:
            pygame.draw.line(screen, (i*1000,0,0), center, (r*cos(a+i)+cx,r*sin(a+i)+cy), width=5)
        else:
            pygame.draw.line(screen, (0,i*1000,0), center, (r*cos(a+i)+cx,r*sin(a+i)+cy), width=5)
        
    for d in np.linspace(0,360,50):
        if d!=360:
            pygame.draw.line(screen, color, center, (r*cos(d*pi/180)+cx,r*sin(d*pi/180)+cy), width=2)
    
    for i in np.linspace(0,r1,10):
        pygame.draw.circle(screen, color, center, i, width=5)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
