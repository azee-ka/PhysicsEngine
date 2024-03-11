# simulation.py

from .model.vector import Vector

def simulate(particle, WINDOW_HEIGHT):
    while True:
        particle.apply_force(Vector(0, 0.1), WINDOW_HEIGHT)  # Apply gravity
        particle.update()
        print(f"Particle Position: ({particle.position.x}, {particle.position.y})")
