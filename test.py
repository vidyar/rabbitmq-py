import unittest
from couch import Couch


class TestSuite(unittest.TestCase):

    def test(self):
        couch = Couch()
        couch.populate()
        things = couch.count()
        self.failIf(things != 5)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
