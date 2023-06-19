from engine.sternman_engine import SternmanEngine

import unittest


class TestSternmanEngine(unittest.TestCase):
    def test_ns_true(self):  #ns = needs service
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_ns_false(self):  #ns = needs service
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())
