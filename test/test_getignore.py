import os.path
import unittest
from pathlib import Path

from main import get_remote_gitignore

OUT_FILE = '.test_gitignore'


class GetignoreTest(unittest.TestCase):

    _path = None

    @classmethod
    def setUpClass(cls) -> None:
        cls._path = Path(OUT_FILE)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._path.unlink()

    def test_get_remote_gitignore_success(self):
        language = 'Python'
        get_remote_gitignore(out_file=OUT_FILE, language=language)
        self.assertTrue(os.path.exists(self._path))

    def test_get_remote_gitignore_no_file_created_on_unfound_file(self):
        language = 'GuaranteedTestFailure1337'
        get_remote_gitignore(out_file=OUT_FILE, language=language)
        self.assertFalse(os.path.exists(self._path))

    def test_get_remote_gitignore_error_on_none_input(self):
        language = ''
        with self.assertRaises(ValueError):
            get_remote_gitignore(language=language)


if __name__ == '__main__':
    unittest.main()
