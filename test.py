import unittest
from rabbit import Rabbit

class TestSuite(unittest.TestCase):

    def test(self):
        rabbit = Rabbit()
        rabbit.sendMessage()
        things = rabbit.readMessage()
        self.failIf(things != "Hello World!")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
