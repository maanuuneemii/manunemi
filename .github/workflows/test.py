import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2]), 3)  # Corrige el uso de la función sum()

if __name__ == '__main__':
    unittest.main()
