import unittest

from hello import hello


class TestHello(unittest.TestCase):

    def test_helen(self):
        """Test that hello prints the expected message for the name Helen"""
        # Define a name
        name = 'Helen'
        # Call the function
        message = hello(name)

        # Assert that the function returns the correct string
        self.assertEqual(message, 'Hello, Helen!')

    def test_integer(self):
        """Test checking that the function fails when an integer is passed"""
        # Define a name
        name = 123
        # Call the function
        with self.assertRaises(TypeError):
            message = hello(name)


if __name__ == '__main__':
    unittest.main()
