# integration/runge_kutta.py

def runge_kutta_step(position, velocity, acceleration, dt):
    """
    Perform one step of the fourth-order Runge-Kutta integration method.

    Args:
    - position (list or tuple): Current position in 3D space (x, y, z).
    - velocity (list or tuple): Current velocity in 3D space (vx, vy, vz).
    - acceleration (list or tuple): Current acceleration in 3D space (ax, ay, az).
    - dt (float): Time step for integration.

    Returns:
    - new_position (list): New position after the time step.
    - new_velocity (list): New velocity after the time step.
    """
    # First step
    k1_v = [a * dt for a in acceleration]
    k1_p = [v * dt for v in velocity]

    # Second step
    k2_v = [a * dt for a in acceleration]
    k2_p = [(v + a * dt / 2) * dt for v, a in zip(velocity, k1_v)]

    # Third step
    k3_v = [a * dt for a in acceleration]
    k3_p = [(v + a * dt / 2) * dt for v, a in zip(velocity, k2_v)]

    # Fourth step
    k4_v = [a * dt for a in acceleration]
    k4_p = [(v + a * dt) * dt for v, a in zip(velocity, k3_v)]

    # Combine the steps to calculate new position and velocity
    new_position = [p + (k1 + 2 * k2 + 2 * k3 + k4) / 6 for p, k1, k2, k3, k4 in zip(position, k1_p, k2_p, k3_p, k4_p)]
    new_velocity = [v + (k1 + 2 * k2 + 2 * k3 + k4) / 6 for v, k1, k2, k3, k4 in zip(velocity, k1_v, k2_v, k3_v, k4_v)]

    return new_position, new_velocity
