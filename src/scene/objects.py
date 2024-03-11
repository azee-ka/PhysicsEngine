# core/scene/objects/objects.py
class Object:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, dt):
        """Update the object's position based on its velocity."""
        self.position += self.velocity * dt