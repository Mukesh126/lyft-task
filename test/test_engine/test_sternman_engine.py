import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def setUp(self):
        self.warning_light_is_on = None
        
    def test_needs_service_when_warning_light_is_on(self):
        self.warning_light_is_on = True
        engine = SternmanEngine(self.warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_when_warning_light_is_off(self):
        self.warning_light_is_on = False
        engine = SternmanEngine(self.warning_light_is_on)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
