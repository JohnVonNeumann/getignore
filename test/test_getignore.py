import unittest
from main import get_remote_gitignore


class MyTestCase(unittest.TestCase):

    def test_get_remote_gitignore_error_on_none_input(self):
        language = ''
        with self.assertRaises(ValueError):
            get_remote_gitignore(language=language)


if __name__ == '__main__':
    unittest.main()
