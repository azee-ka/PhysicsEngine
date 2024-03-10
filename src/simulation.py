# simulation.py

from src.model.vector import Vector

def simulate(particle):
    # Simulation loop
    while True:
        # Apply forces and update particle
        particle.apply_force(Vector(0, 0.1))  # Apply gravity
        particle.update()
