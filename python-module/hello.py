import unittest


class TestHello(unittest.TestCase):

    def hello(self):
        print("Hellow world in python!")
        x = 10
        self.assertTrue(x == 10)
