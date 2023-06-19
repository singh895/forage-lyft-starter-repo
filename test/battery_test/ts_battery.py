import unittest
from datetime import date

from battery.spindlerbattery import Spindler_Battery


class TestSpindlerBattery(unittest.TestCase):
    def test_ns_true(self):  #ns = needs service
        curr_date = date.fromisoformat("2020-05-15")
        last_date = date.fromisoformat("2018-01-25")
        batt = Spindler_Battery(curr_date, last_date)
        self.assertTrue(batt.needs_service())
    
    def test_ns_false(self):  #ns = needs service
        curr_date = date.fromisoformat("2020-05-15")
        last_date = date.fromisoformat("2019-01-10")
        batt = Spindler_Battery(curr_date, last_date)
        self.assertFalse(batt.needs_service())