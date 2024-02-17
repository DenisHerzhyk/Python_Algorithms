from main import dict_our_list
import unittest


class TestDict(unittest.TestCase):
    def test_first(self):
        self.assertEquals(dict_our_list("This is a test test Test"), {'this': 1, 'is': 1, 'a': 1, 'test': 3})

    def test_second(self):
        self.assertEquals(dict_our_list("Hello world and hello again"), {'hello': 2, 'world': 1, 'and': 1, 'again': 1})
