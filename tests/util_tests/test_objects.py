# tests/test_objects.py
import unittest
from src.scene.objects import Object

class TestObject(unittest.TestCase):
    def test_object_update(self):
        obj = Object([0, 0, 0], [1, 1, 1])
        obj.update(0.1)
        self.assertEqual(obj.position, [0.1, 0.1, 0.1])

if __name__ == '__main__':
    unittest.main()
