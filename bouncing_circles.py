"""
Physics simulator for a series of bouncing circles. 

Uses pygame as a GUI
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
accel_x = 0
accel_y = 9.8



# Circle class
class Circle:
    def __init__(self, position, velocity, acceleration, size, color = white):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.size = size
        self.color = color
        self.width = size
    
    def display(self):
        x = round(self.position[0])
        y = round(self.position[1])
        pygame.draw.circle(screen, self.color, (x, y), self.size, self.width)

    def update_acceleration(self):
        d2x = self.acceleration[0] - 0.5 * self.velocity[0]
        d2y = self.acceleration[1] - 0.5 * self.velocity[0]
        self.acceleration = (d2x, d2y)

    def update_velocity(self):
        # if position is near a boundary, make it bounce
        dx = self.velocity[0] + accel_x * dtime * dtime
        dy = self.velocity[1] + accel_y * dtime * dtime
        self.velocity = (dx, dy)
        if (self.position[0] >= screen_width - self.size) or (self.position[0] - self.size <= 0):
            if self.position[0] - self.size <= 0:
                self.position = (self.size + 5, self.position[1])
            self.velocity = (-self.velocity[0], self.velocity[1])

        if (self.position[1] >= screen_height - self.size) or (self.position[1] - self.size <= 0):
            if self.position[1] - self.size <= 0: 
                self.position = (self.position[0], self.size + 5)
            self.velocity = (self.velocity[0], -self.velocity[1])

    def update_position(self):
        self.update_velocity()
        x = self.position[0] + self.velocity[0] * dtime + self.acceleration[0] * dtime * dtime
        y = self.position[1] + self.velocity[1] * dtime + self.acceleration[1] * dtime * dtime
        self.position = (x, y)
    
    


# Initilize Circles:
num_circles = 200
circles = [
    Circle(
        position=(randint(50, 1150), randint(50, 750)), 
        velocity=(randint(-10, 10), randint(-10, 10)),
        acceleration=(accel_x, accel_y), 
        size=randint(0, 50),
        color=(randint(10,255), randint(180,255), randint(180,255))
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
                position=event.pos, 
                velocity=(randint(-50,50), randint(-50,50)),
                acceleration=(accel_x, accel_y), 
                size=randint(0, 50),
                color=(randint(10,255), randint(180,255), randint(180,255))))
        if event.type == pygame.QUIT:
            run_me = False
    
    screen.fill(black)
    
    for circle in circles:
        circle.display()
        circle.update_position()

    pygame.display.flip()
