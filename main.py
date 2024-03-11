# main.py

from src.model.vector import Vector
from src.model.particle import Particle
from src.simulation import simulate
from src.visualization import visualize
import threading

def main():
    particle = Particle((Vector(400, 300, 0)), (Vector(0, 0, 0)), (Vector(0, 0, 0)))  # Add mass here

    # Create a thread for the simulation
    simulate_thread = threading.Thread(target=simulate, args=(particle, 600))  # Pass WINDOW_HEIGHT here
    simulate_thread.start()

    # Visualize the particle
    visualize()

if __name__ == "__main__":
    main()
