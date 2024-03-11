# visualization.py

import pygame
import sys
from pygame.locals import *
from .model.vector import Vector
from .model.particle import Particle

def visualize():
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

    particle = Particle((Vector(400, 30, 0)), (Vector(0, 0, 0)), (Vector(0, 0, 0)))  # Create particle instance here

    # Simulation loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        window.fill(BLACK)

        # Apply forces and update particle
        particle.apply_force(Vector(0, 0.1, 0), 600)  # Apply gravity
        particle.update()

        # Debugging
        print(f"Particle Position: ({particle.position.x}, {particle.position.y})")

        # Draw the particle
        pygame.draw.circle(window, WHITE, (int(particle.position.x), int(particle.position.y)), 5)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    visualize()
