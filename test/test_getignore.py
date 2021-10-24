import os.path
import unittest
from pathlib import Path

from main import get_remote_gitignore

OUT_FILE = '.test_gitignore'


class GetignoreTest(unittest.TestCase):

    def setUp(self) -> None:
        self._p = Path(OUT_FILE)
        self._p.touch()

    def test_get_remote_gitignore_success(self):
        language = 'Python'
        get_remote_gitignore(out_file=OUT_FILE, language=language)
        self.assertTrue(os.path.exists(self._p))

    def test_get_remote_gitignore_error_on_none_input(self):
        language = ''
        with self.assertRaises(ValueError):
            get_remote_gitignore(language=language)

    def tearDown(self) -> None:
        self._p.unlink()


if __name__ == '__main__':
    unittest.main()
