import unittest

from fizzbuzz import InvalidParamsException, fizzbuzzer, step1_f, step2_f


class FBTestCase(unittest.TestCase):
    def test_correct_values(self):
        self.assertEqual(fizzbuzzer(1, 20, step1_f),
                         '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz',
                         'Incorrect Result 1')

        self.assertEqual(fizzbuzzer(18, 31, step1_f),
                         'fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 31',
                         'Incorrect Result 2')

        self.assertEqual(fizzbuzzer(18, 18, step1_f),
                         'fizz',
                         'Incorrect Result 3')

    def test_correct_values2(self):
        self.assertEqual(fizzbuzzer(1, 20, step2_f),
                         '1 2 lucky 4 buzz fizz 7 8 fizz buzz 11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz',
                         'Incorrect Result 1')

        self.assertEqual(fizzbuzzer(18, 31, step2_f),
                         'fizz 19 buzz fizz 22 lucky fizz buzz 26 fizz 28 29 lucky lucky',
                         'Incorrect Result 2')

    def test_type_cast(self):
        self.assertEqual(fizzbuzzer(3, '4', step1_f),
                         'fizz 4',
                         'Incorrect Cast')

    def test_invalid_params(self):
        self.assertRaises(InvalidParamsException, fizzbuzzer, 3, -3)
        self.assertRaises(InvalidParamsException, fizzbuzzer, 3, 2)
        self.assertRaises(InvalidParamsException, fizzbuzzer, 3, '2a')
