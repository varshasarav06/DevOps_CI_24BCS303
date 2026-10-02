import unittest
from src.grade_calculator import calculate_grade


class TestGradeCalculator(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(calculate_grade(95), "A")
    
    def test_grade_boundary(self):
        self.assertEqual(calculate_grade(90), "A")
    
    def test_grade_b(self):
        self.assertEqual(calculate_grade(85), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(75), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(65), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(45), "F")

    def test_invalid_mark(self):
        self.assertEqual(calculate_grade(105), "Invalid")


if __name__ == "__main__":
    unittest.main()
