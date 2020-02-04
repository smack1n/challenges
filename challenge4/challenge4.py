import unittest
from fibonacci import fibonacci

class challenge4(unittest.TestCase):

    def test_challenge4(self):

        i = 3

        while i < 20:
            n = fibonacci(i)
            print(n)
            i += 1

if __name__ == '__main__':
    unittest.main()
