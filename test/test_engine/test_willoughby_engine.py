import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def setUp(self):
        self.current_mileage = 60000
        self.last_service_mileage = 0
        
    def test_needs_service_when_mileage_over_threshold(self):
        self.current_mileage = 60001
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_when_mileage_below_threshold(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
