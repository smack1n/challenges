import unittest
from fibonacci import fibonacci

def test_challenge4(fibonacci):

    n = 10

    fibonacci(n)

    print(n)

if __name__ == '__main__':
    unittest.main()
