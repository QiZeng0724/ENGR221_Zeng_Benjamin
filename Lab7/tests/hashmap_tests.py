import pytest

from ..myHashMap import MyHashMap

class HashMapTest():

    def test_put_and_get(self):
        hashmap = MyHashMap()
        hashmap.put("a", 1)
        self.assertEqual(hashmap.get("a"), 1)
        hashmap.put("b", 2)
        self.assertEqual(hashmap.get("b"), 2)

    def test_replace(self):
        hashmap = MyHashMap()
        hashmap.put("a", 1)
        hashmap.replace("a", 10)
        self.assertEqual(hashmap.get("a"), 10)
        self.assertEqual(hashmap.replace("b", 20))
    
    def test_remove(self):
        hashmap = MyHashMap()
        hashmap.put("a", 1)
        self.assertTrue(hashmap.remove("a"))  # should return True
        self.assertIsNone(hashmap.get("a"))  # should return None
        self.assertFalse(hashmap.remove("b"))
    
    def test_size(self):
        hashmap = MyHashMap()
        self.assertEqual(hashmap.size, 0)
        hashmap.put("a", 1)
        self.assertEqual(hashmap.size, 1)
        hashmap.put("b", 2)
        self.assertEqual(hashmap.size, 2)
        hashmap.remove("a")
        self.assertEqual(hashmap.size, 1)

    def test_is_empty(self):
        hashmap = MyHashMap()
        self.assertTrue(hashmap.isEmpty())
        hashmap.put("a", 1)
        self.assertFalse(hashmap.isEmpty())
        hashmap.remove("a")
        self.assertTrue(hashmap.isEmpty())