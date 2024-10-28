import pytest

from ..box import Box

class BoxTest():
    def setUp(self):
        self.box = Box()

    def test_add_entry(self):
        self.assertTrue(self.box.add("Fluffy", "Cat"))
        self.assertFalse(self.box.add("Fluffy", "Dog"))  # Duplicate nickname

    def test_find_entry(self):
        self.box.add("Fluffy", "Cat")
        entry = self.box.find("Fluffy", "Cat")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.getSpecies(), "Cat")
        self.assertIsNone(self.box.find("Fluffy", "Dog"))  # Species does not match

    def test_find_all_nicknames(self):
        self.box.add("Fluffy", "Cat")
        self.box.add("Fido", "Dog")
        nicknames = self.box.findAllNicknames()
        self.assertIn("Fluffy", nicknames)
        self.assertIn("Fido", nicknames)

    def test_remove_by_nickname(self):
        self.box.add("Fluffy", "Cat")
        self.assertTrue(self.box.removeByNickname("Fluffy"))
        self.assertIsNone(self.box.findEntryByNickname("Fluffy"))

    def test_remove_entry(self):
        self.box.add("Fluffy", "Cat")
        self.assertTrue(self.box.removeEntry("Fluffy", "Cat"))
        self.assertIsNone(self.box.findEntryByNickname("Fluffy"))
