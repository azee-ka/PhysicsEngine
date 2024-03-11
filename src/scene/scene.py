# core/scene/scene.py
class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        """Add an object to the scene."""
        self.objects.append(obj)

    def remove_object(self, obj):
        """Remove an object from the scene."""
        self.objects.remove(obj)

    def update(self, dt):
        """Update the scene."""
        for obj in self.objects:
            obj.update(dt)