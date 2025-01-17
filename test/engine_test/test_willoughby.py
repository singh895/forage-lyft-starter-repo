from engine.willoughby_engine import WilloughbyEngine

import unittest

#A testcase is created by subclassing unittest.TestCase
class TestWilloughbyEngine(unittest.TestCase):
    def test_ns_true(self):  #ns = needs service
        curr_mileage = 60001
        last_mileage = 0
        engine = WilloughbyEngine(curr_mileage, last_mileage)
        self.assertTrue(engine.needs_service())  #verify condition

    def test_ns_false(self):  #ns = needs service
        curr_mileage = 60000
        last_mileage = 0
        engine = WilloughbyEngine(curr_mileage, last_mileage)
        self.assertFalse(engine.needs_service())
