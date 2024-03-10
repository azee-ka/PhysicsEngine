from .vector import Vector

class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def apply_force(self, force):
        self.acceleration = self.acceleration.add(force)

    def update(self):
        self.velocity = self.velocity.add(self.acceleration)
        self.position = self.position.add(self.velocity)
        self.acceleration = Vector(0, 0)  # Reset acceleration

    def display(self):
        print(f"Position: ({self.position.x}, {self.position.y}) Velocity: ({self.velocity.x}, {self.velocity.y})")
