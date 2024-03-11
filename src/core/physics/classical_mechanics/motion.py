# core/classical_mechanics/motion.py
def update_position(position, velocity, dt):
    """Update position based on velocity and time step."""
    return position + velocity * dt

def update_velocity(velocity, acceleration, dt):
    """Update velocity based on acceleration and time step."""
    return velocity + acceleration * dt

def update_acceleration(force, mass):
    """Update acceleration based on force and mass."""
    return force / mass
