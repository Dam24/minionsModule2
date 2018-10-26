from unittest import TestCase
from binary_search.binary_search import BinarySearch


class TestBinarySearch(TestCase):
    def setUp(self):
        self.search = BinarySearch()

    def test_binary_search(self):
        array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEquals(self.search.binary_search(array_list, 10), 9)
        self.assertEquals(self.search.lastListSize, 10)
        self.assertEquals(self.search.lastGuesses, 4)

    def test_is_sorted_list(self):
        array_list = [1, 3, 2, 4, 5, 9, 7, 8, 10]
        self.assertFalse(self.search.is_sorted_list(array_list))
        array_list = [1, 2, 3, 4, 5, 7, 8, 10]
        self.assertTrue(self.search.is_sorted_list(array_list))

    def test_last_search_result(self):
        array_list = [1, 3, 2, 4, 5, 9, 7, 8, 10]
        self.search.binary_search(array_list, 2)
        self.assertEquals(self.search.last_search_result(), (0, 9))

        array_list = [1, 2, 4, 5, 7, 8, 10]
        self.search.binary_search(array_list, 2)
        self.assertEquals(self.search.last_search_result(), (2, 7))
