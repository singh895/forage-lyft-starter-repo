import unittest
from tires.octoprime_tires import OctoprimeTires

class tectOctoprime(unittest.TestCase):
    def test_ns_True(self):
        tire_wear = [0.7, 0.6,1, 0.8]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())
    
    def test_ns_False(self):
        tire_wear = [0.2, 0.3, 0.4, 0.3]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())