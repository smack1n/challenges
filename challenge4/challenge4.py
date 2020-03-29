import unittest
from fibonacci import fibonacci
import n2w #Really struggled to create my own function


class challenge4(unittest.TestCase):

    def test_challenge4(self):

        i = 3

        while i < 20:
            num = fibonacci(i)
            print(num)

            print(n2w.convert(num))

            i += 1

if __name__ == '__main__':
    unittest.main()
