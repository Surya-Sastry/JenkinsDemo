import unittest

from Demo import add


class TestAdd(unittest.TestCase):
    def test_simple(self):
        a = 2
        b = 3
        c = add(a, b)
        self.assertEqual(c, a+b)

    def test_medium(self):
        a = 12345678987654321
        b = 98765432123456789
        c = add(a, b)
        self.assertEqual(c, a+b)

    def test_hard(self):
        a = 12345678987654321.8967452310
        b = 98765432123456789.2143658709
        c = add(a, b)
        self.assertEqual(c, a+b)


if __name__ == "__main__":
    unittest.main()
