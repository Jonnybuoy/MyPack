import unittest
from circle_area import area_circle
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(area_circle(1), pi)
        self.assertAlmostEqual(area_circle(0), 0)
        self.assertAlmostEqual(area_circle(2.1), pi*2.1**2)

    def test_values(self):
        # Raise value errors when necessary
        self.assertRaises(ValueError, area_circle, -2)

    def test_types(self):
        # Raise type errors when necessary
        self.assertRaises(TypeError, area_circle, 3+5j)
        self.assertRaises(TypeError, area_circle, True)
        self.assertRaises(TypeError, area_circle, "radius")
