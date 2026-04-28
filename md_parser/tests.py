import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    from md_parser import MDParser

    with open("README.md") as file:
        parser = MDParser(file)
        parser.parse_md()

    unittest.main()
