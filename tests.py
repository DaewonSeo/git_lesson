from convert import convert_to_uppercase
import unittest


class TestConvertToUppercase(unittest.TestCase):

    def test_basic_conversion(self):
        mixed_string = "ThiS is A MixEd-CaSe StrinG"
        expected_output = "THIS IS A MIXED-CASE STRING"
        self.assertEqual(convert_to_uppercase(mixed_string), expected_output)

    def test_another_string(self):
        mixed_string = "another MiXeD StRiNg"
        expected_output = "ANOTHER MIXED STRING"
        self.assertEqual(convert_to_uppercase(mixed_string), expected_output)

    def test_all_caps(self):
        mixed_string = "ALL CAPS"
        expected_output = "ALL CAPS"
        self.assertEqual(convert_to_uppercase(mixed_string), expected_output)

    def test_lowercase(self):
        mixed_string = "lowercase"
        expected_output = "LOWERCASE"
        self.assertEqual(convert_to_uppercase(mixed_string), expected_output)


if __name__ == '__main__':
    unittest.main()
