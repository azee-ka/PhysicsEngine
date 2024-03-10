# visualization.py

import pygame
import sys
from pygame.locals import *
from src.model.particle import Particle

def visualize(particle):
    # Initialize Pygame
    pygame.init()

    # Set up the display
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Physics Simulation')

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Simulation loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        window.fill(BLACK)

        # Draw the particle
        pygame.draw.circle(window, WHITE, (int(particle.position.x), int(particle.position.y)), 5)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)
