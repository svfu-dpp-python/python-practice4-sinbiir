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

    def test_write_range(self):
        a = -8
        b = 9
        filename = "test.txt"
        main.write_range(filename, a, b)
        with open(filename) as f:
            self.assertEqual(list(map(str, range(a, b))), f.read().split())
