# main.py

from src.model.vector import Vector
from src.model.particle import Particle
from src.simulation import simulate
from src.visualization import visualize

def main():
    particle = Particle(Vector(400, 300), Vector(0, 0), Vector(0, 0))
    simulate(particle)
    visualize(particle)

if __name__ == "__main__":
    main()