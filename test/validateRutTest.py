import unittest

from helpers import validations


class TestRut(unittest.TestCase):
    def test_rut_true(self):
        result = validations.validateRut('188617786')
        self.assertEqual(result, True)
    def test_rut_false(self):
        result = validations.validateRut('33.333.333-k')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()