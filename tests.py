import unittest

from fizzbuzz import InvalidParamsException, fizzbuzzer, Step1, Step2, Step3


class FBTestCase(unittest.TestCase):
    def test_correct_values(self):
        self.assertEqual(fizzbuzzer(1, 20, Step1),
                         '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz',
                         'Incorrect Result 1')

        self.assertEqual(fizzbuzzer(18, 31, Step1),
                         'fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 31',
                         'Incorrect Result 2')

        self.assertEqual(fizzbuzzer(18, 18, Step1),
                         'fizz',
                         'Incorrect Result 3')

    def test_correct_values2(self):
        self.assertEqual(fizzbuzzer(1, 20, Step2),
                         '1 2 lucky 4 buzz fizz 7 8 fizz buzz 11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz',
                         'Incorrect Result 1')

        self.assertEqual(fizzbuzzer(18, 31, Step2),
                         'fizz 19 buzz fizz 22 lucky fizz buzz 26 fizz 28 29 lucky lucky',
                         'Incorrect Result 2')

    def test_correct_values3(self):
        self.assertEqual(fizzbuzzer(1, 20, Step3),
                         '1 2 lucky 4 buzz fizz 7 8 fizz buzz 11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz\nfizz: 4\nbuzz: 3\nfizzbuzz: 1\nlucky: 2\ninteger: 10',
                         'Incorrect Result 1')

        self.assertEqual(fizzbuzzer(18, 31, Step3),
                         'fizz 19 buzz fizz 22 lucky fizz buzz 26 fizz 28 29 lucky lucky\nfizz: 4\nbuzz: 2\nfizzbuzz: 0\nlucky: 3\ninteger: 5',
                         'Incorrect Result 2')

    def test_type_cast(self):
        self.assertEqual(fizzbuzzer(3, '4', Step1),
                         'fizz 4',
                         'Incorrect Cast')

    def test_invalid_params(self):
        self.assertRaises(InvalidParamsException, fizzbuzzer, 3, -3)
        self.assertRaises(InvalidParamsException, fizzbuzzer, 3, 2)
        self.assertRaises(InvalidParamsException, fizzbuzzer, 3, '2a')
