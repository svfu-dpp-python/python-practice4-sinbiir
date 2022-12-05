import tempfile
import unittest
import main


class TestMain(unittest.TestCase):
    def test_find_maximums(self):
        with tempfile.NamedTemporaryFile("w") as f:
            f.write("1 2 3\n4 6 5\n9 8 7\n")
            f.flush()
            res = main.find_maximums(f.name)
            self.assertEqual([3, 6, 9], res)
