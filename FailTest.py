import unittest

from Demo import add


class TestAdd(unittest.TestCase):
    def test_fail_simple(self):
        a = 2
        b = 3
        c = add(a, b)
        self.assertEqual(c, -5)

    def test_fail_medium(self):
        a = 12345678987654321
        b = 98765432123456789
        c = add(a, b)
        self.assertEqual(c, 0)


if __name__ == "__main__":
    unittest.main()
