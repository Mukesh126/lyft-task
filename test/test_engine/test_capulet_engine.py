import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        self.current_mileage = 30000
        self.last_service_mileage = 0
        
    def test_needs_service_when_mileage_over_threshold(self):
        self.current_mileage = 30001
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_when_mileage_below_threshold(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
