# -*-coding=utf8-*-

import unittest
from lib import Project

class Test_Project(unittest.TestCase):
    project = Project('Eagle')

    def test_name(self):
        self.assertEqual(self.project.name, 'Eagle')

    def test_name_size(self):
        self.assertEqual(self.project.name_size, 5)

class Test_Blabla(unittest.TestCase):
    def test_a(self):
        self.assertFalse(True) # it will fail the test

    def test_b(self):
        with self.assertRaises(TypeError):
            1 + '1'

if __name__ == '__main__':
    unittest.main()
