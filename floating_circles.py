"""
Physics simulator for a series of bouncing circles. 

Uses pygame as a GUI

https://www.youtube.com/watch?v=7AKatTpNSNQ&list=PLE3D1A71BB598FEF6
"""

import os, sys, math
from random import random, randint, choice
import pygame


pygame.init()

# Useful colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [white, red, green, blue]

# Screen size declarations
screen_width, screen_height = 1200, 800
screen_size = (screen_width, screen_height)

# Initilization of Pygame screen and clock
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Math variables
dtime = .1

# Circle class
class Circle:
    def __init__(self, position, velocity, size, color = white):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.color = color
        self.width = size
    
    def display(self):
        x = round(self.position[0])
        y = round(self.position[1])
        pygame.draw.circle(screen, self.color, (x, y), self.size, self.width)
    
    def update_position(self):
        x = self.position[0] + self.velocity[0] * dtime
        y = self.position[1] + self.velocity[1] * dtime
        self.position = (x, y)


# Initilize Circles:
num_circles = 1
circles = [
    Circle(
        position=(randint(0, 1200), randint(0, 800)), 
        velocity=(randint(-10, 10), randint(-10, 10)), 
        size=randint(0, 50),
        color=choice(colors)
        )
    for _ in range(num_circles)
]

# Display / Run loop
fps_limit = 60
run_me = True
while run_me:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Release of left click
            circles.append(Circle(
                event.pos, 
                (randint(-10,10), randint(-10,10)),
                randint(0, 50),
                (randint(10,255), randint(180,255), randint(180,255))))
        if event.type == pygame.QUIT:
            run_me = False
    
    screen.fill(black)
    
    for circle in circles:
        circle.display()
        circle.update_position()

    pygame.display.flip()
