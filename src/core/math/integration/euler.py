# core/math/integration/euler.py

def euler_step(position, velocity, acceleration, dt):
    """
    Perform one step of Euler integration.

    Args:
    - position (list or tuple): Current position in 3D space (x, y, z).
    - velocity (list or tuple): Current velocity in 3D space (vx, vy, vz).
    - acceleration (list or tuple): Current acceleration in 3D space (ax, ay, az).
    - dt (float): Time step for integration.

    Returns:
    - new_position (list): New position after the time step.
    - new_velocity (list): New velocity after the time step.
    """
    # Calculate new velocity using current acceleration
    new_velocity = [v + a * dt for v, a in zip(velocity, acceleration)]
    
    # Calculate new position using current velocity
    new_position = [p + v * dt for p, v in zip(position, velocity)]

    return new_position, new_velocity
