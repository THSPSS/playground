import unittest

from odd_or_even import asking_user_and_getting_data , convert_string_into_int

class Test(unittest.TestCase):

    def testUserInput(self):
        """
        Test that test user input result type
        :return: "string"
        """
        data = "23"
        result = convert_string_into_int(data)
        self.assertEqual(result, 23)

if __name__ == "__main__":
    unittest.main()

