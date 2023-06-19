from engine.capulet_engine import CapuletEngine

import unittest

#A testcase is created by subclassing unittest.TestCase
class TestCapuletEngine(unittest.TestCase):
    def test_ns_true(self):  #ns = needs service
        curr_mileage = 30001
        last_mileage = 0
        engine = CapuletEngine(curr_mileage, last_mileage)
        self.assertTrue(engine.needs_service())  #verify condition

    def test_ns_false(self):  #ns = needs service
        curr_mileage = 30000
        last_mileage = 0
        engine = CapuletEngine(curr_mileage, last_mileage)
        self.assertFalse(engine.needs_service())
