import unittest

from main import main


class Test01(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = "dolce"
        result = main(data)
        self.assertEqual(8, result)


class Test02(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = "jazzy"
        result = main(data)
        self.assertEqual(33, result)


class Test03(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = "jazzist"
        result = main(data)
        self.assertEqual(32, result)


class Test04(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = "JaZzy"
        result = main(data)
        self.assertEqual(33, result)
