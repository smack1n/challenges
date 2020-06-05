import unittest
from common.fibonacci import fibonacci
import n2w

# Really struggled to create my own function so I had to import n2w


class challenge4(unittest.TestCase):

    def test_challenge4(self):

        i = 3

        while i < 20:
            num = fibonacci(i)
            print(str(num), " - ", (n2w.convert(num)))

            i += 1

if __name__ == '__main__':
    unittest.main()
