# this is for calculating how much money are you actually making
#*********************************************************************
# Author: Giancarlo Rhodes
# Description: Getting to accurate taxable amount. Unit testing
#*********************************************************************


import unittest
import delivery_calc_lib

# testing the framework
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

class TestDeliveryCalcLib(unittest.TestCase):

    def test_mileage_ratio_str_to_float(self):
        # print("Float: ", str(delivery_calc_lib._mileage_ratio_str_to_float("5/3")))
        # print("Rounded: ", str(round(delivery_calc_lib._mileage_ratio_str_to_float("5/3"), 2)))
        self.assertEqual(1.67, delivery_calc_lib._mileage_ratio_str_to_float("5/3"))


    def test_get_miles_drove_estimate(self):
        # drove 5 miles for $10 dollars, this is one way, which probably
        # an underestimate of "real" mileage
        _ratio = delivery_calc_lib._mileage_ratio_str_to_float("10/5") # 2
        self.assertEqual(_ratio, 2)
        _money_made: int = 100 # made $100
        _mileage = _money_made / _ratio
        self.assertEqual(_mileage, 50)

    def test_100dollars_drove50miles(self):
        _expected = 33.5
        _ratio = delivery_calc_lib._mileage_ratio_str_to_float("20/10") # 2
        _actual = delivery_calc_lib._debit_calc_func(100, _ratio, 67)
        print("Expected: ", _expected, ", Actual: ", _actual)
        self.assertEqual(_expected, _actual)
        print("It cost $",_actual,"to drive 50 miles.")

    def test_drove100miles(self):
        _ratio = delivery_calc_lib._mileage_ratio_str_to_float("10/6") # .67
        print ("My dollars to miles ratio is: ", _ratio)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)