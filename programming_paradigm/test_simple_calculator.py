import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        with self.assertRaises(TypeError):
            _ = 5 + "5"

    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(-1,1), 2)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertAlmostEqual(self.calc.subtract(0.1, 0.2), -0.1, places=7)

    def test_multiplication(self):
        """Test the multiplication class"""
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-1,1), -1)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), -0.02, places=7)
    
    def test_division(self):
        """Test the division class"""
        self.assertEqual(self.calc.divide(9,3), 3)
        self.assertAlmostEqual(self.calc.divide(0.9, 0.3), 3, places=7)

if __name__ == "__main__":
    unittest.main()