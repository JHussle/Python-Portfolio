import unittest
import rball

class TestApp(unittest.TestCase):
    
    def test_add(self):
        result = rball.add(.45, .5)
        self.assertEqual(result)
        