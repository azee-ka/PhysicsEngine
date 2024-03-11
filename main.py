# main.py

from src1.model.vector import Vector
from src1.model.particle import Particle
from src1.simulation import simulate
from src1.visualization import visualize
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
