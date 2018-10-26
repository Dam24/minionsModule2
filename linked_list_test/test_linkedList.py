from unittest import TestCase
from linked_list.linked_list import LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_insert(self):
        self.list.insert("Damian")
        self.assertTrue(self.list.head.get_data() == "Damian")
        self.assertTrue(self.list.head.get_next() is None)
        self.assertEqual(self.list.size(), 1)

    def test_size(self):
        self.list.insert("Jacob")
        self.list.insert("Pedro")

        self.assertTrue(self.list.head.get_data() == "Pedro")

        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "Jacob")

    def test_search(self):
        self.list.insert("Jhon")
        self.list.insert("Nathan")
        self.list.insert("Melvin")

        found = self.list.search("Jhon")
        self.assertTrue(found.get_data() == "Jhon")

        found = self.list.search("Nathan")
        self.assertTrue(found.get_data() == "Nathan")

        found = self.list.search("Jhon")
        self.assertTrue(found.get_data() == "Jhon")

    def test_delete(self):
        self.list.insert("Jhon")
        self.list.insert("Nathan")
        self.list.insert("Melvin")

        # Delete the list head
        self.list.delete("Melvin")
        self.assertTrue(self.list.head.get_data() == "Nathan")

        # Delete the list tail
        self.list.delete("Jhon")
        self.assertTrue(self.list.head.get_next() is None)
