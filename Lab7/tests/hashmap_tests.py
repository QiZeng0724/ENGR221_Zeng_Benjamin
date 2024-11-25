import pytest

from myHashMap import MyHashMap

def test_put():
    hashmap = MyHashMap()
    assert hashmap.isEmpty() == True #hashmap will be empty as it's newly created

    hashmap.put("1234","test")
    assert hashmap.isEmpty() == False #hashmap will not be empty after adding 1234(key) and test(value) 

    hashmap.remove("1234")
    assert hashmap.isEmpty() == True #hashmap will empty after removing key

def test_get_size():
    hashmap = MyHashMap()
    assert hashmap.get_size() == 0 #size equals 0 (empty hashmap)

    hashmap.put("1234","test")
    assert hashmap.get_size() == 1 #size equals 1 after putting 1 key value pair

    hashmap.put("5678","test2")
    assert hashmap.get_size() == 2 #size equals 2 after putting 2 key value pairs

    hashmap.remove("1234")
    assert hashmap.get_size() == 1 #size equals 1 after removing 1 key value pair

def test_keys():
    hashmap = MyHashMap()

    #populates the hashmap
    hashmap.put("1234","test")
    hashmap.put("5678","test2")

    keys = hashmap.keys()
    assert set(keys) == {"1234","5678"} #checks if keys are returned correctly

    hashmap.remove("1234")
    keys = hashmap.keys()
    assert set(keys) == {"5678"} #checks if key is returned correctly after removing one