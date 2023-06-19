from engine.sternman_engine import SternmanEngine

import unittest

#A testcase is created by subclassing unittest.TestCase
class TestSternmanEngine(unittest.TestCase):
    def test_ns_true(self):  #ns = needs service
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())  #verify condition

    def test_ns_false(self):  #ns = needs service
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())
