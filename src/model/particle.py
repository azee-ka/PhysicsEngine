# particle.py

from .vector import Vector

class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def apply_force(self, force, window_height):
        if self.position.y < window_height:  # Check if particle is above the bottom border
            self.acceleration += force  # Apply gravity
        else:
            self.velocity.y = 0  # Stop the particle from falling further

    def update(self):
        # Limit the acceleration to prevent rapid acceleration
        max_acceleration = 1
        self.acceleration.limit(max_acceleration)

        # Update the velocity based on the acceleration
        self.velocity += self.acceleration

        # Update the position based on the velocity
        self.position += self.velocity


    def display(self):
        print(f"Position: ({self.position.x}, {self.position.y}) Velocity: ({self.velocity.x}, {self.velocity.y})")
