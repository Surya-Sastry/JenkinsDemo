import unittest

from Demo import mul


class TestAdd(unittest.TestCase):
    def test_fail_simple(self):
        a = 2
        b = 3
        c = mul(a, b)
        self.assertEqual(c, 5)

    def test_fail_medium(self):
        a = 12
        b = 9
        c = mul(a, b)
        self.assertEqual(c, 0)


if __name__ == "__main__":
    unittest.main()
