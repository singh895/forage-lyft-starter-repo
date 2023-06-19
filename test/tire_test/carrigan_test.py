import unittest
from tires.carrigan_tires import CarriganTires

class tectCarrigan(unittest.TestCase):
    def test_ns_True(self):
        tire_wear = [0.2, 0.1, 1, 0.3]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())
    
    def test_ns_False(self):
        tire_wear = [0.2, 0.7, 0.7, 0.8]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())