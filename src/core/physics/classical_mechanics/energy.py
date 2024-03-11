# core/classical_mechanics/energy.py
def calculate_kinetic_energy(mass, velocity):
    """Calculate kinetic energy."""
    return 0.5 * mass * velocity**2

def calculate_potential_energy(mass, height, gravity):
    """Calculate potential energy."""
    return mass * gravity * height