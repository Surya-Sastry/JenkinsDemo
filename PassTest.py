import unittest

from Demo import mul


class TestAdd(unittest.TestCase):
    def test_simple(self):
        a = 3
        b = 3
        c = mul(a, b)
        self.assertEqual(c, a*b)

    def test_medium(self):
        a = 100
        b = 666
        c = mul(a, b)
        self.assertEqual(c, a*b)

    def test_hard(self):
        a = -3
        b = 474994
        c = mul(a, b)
        self.assertEqual(c, a*b)


if __name__ == "__main__":
    unittest.main()
