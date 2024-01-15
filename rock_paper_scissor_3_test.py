# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min
# rock == rock --> draw, paper == paper --> draw, scissor == scissor --> draw
import unittest
import my_module

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min
# rock == rock --> draw, paper == paper --> draw, scissor == scissor --> draw

class TestMyModuleMethods(unittest.TestCase):

    def test_rand_convert(self):
        self.assertTrue("SCISSOR", my_module.rand_convert())

    def test_rand_convert_v2(self):    
        self.assertIsNotNone(my_module.rand_convert_v2())


if __name__ == '__main__':
    unittest.main(verbosity=2)



