import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        self.current_date = date.fromisoformat("2023-09-14")
        
    def test_needs_service_when_last_service_was_long_ago(self):
        last_service_date = date.fromisoformat("2019-01-25")
        battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_when_last_service_was_recent(self):
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(self.current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
