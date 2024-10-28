"""
WRITE YOUR PROGRAM HEADER HERE

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Create a new set of buckets that's twice as big as the old one
        new_buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())
        # Update the self.buckets attribute with the new entries
        self.buckets = new_buckets

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        if key is None:
            raise Exception("Key can't be none.")

        if self.size / self.capacity >= self.load_factor:
            self.resize()

        keyHash = hash(key) % self.capacity
        for entry in self.buckets[keyHash]:
            if entry.getKey() == key:
                entry.setValue(value)
                return True

        self.buckets[keyHash].append(self.MyHashMapEntry(key, value))
        self.size += 1
        return True 

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        if key is None:
            raise Exception("Key can't be none.")
        
        keyHash = hash(key) % self.capacity
        for entry in self.buckets[keyHash]:
            if entry.getKey() == key:
                entry.setValue(newValue)
                return True
        return False

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        if key is None:
            raise Exception("key can't be none.")
        
        keyHash = hash(key) % self.capacity
        bucket = self.buckets[keyHash]
        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        return self.put(key, value)

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        if key is None:
            raise Exception("Key can't be none.")
        
        keyHash = hash(key) % self.capacity
        for entry in self.buckets[keyHash]:
            if entry.getKey() == key:
                return entry.getValue()
        return None

    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self):
        return self.size

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        return self.size == 0

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        if key is None:
            raise Exception("Key can't be none.")

        keyHash = hash(key) % self.capacity
        for entry in self.buckets[keyHash]:
            if entry.getKey() == key:
                return True
        return False 

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        result = []
        for bucket in self.buckets:
            for entry in bucket:
                result.append(entry.getKey())
        return result

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    print(hashmap.get("key1"))
    hashmap.replace("key1", "new_value1")
    print(hashmap.get("key1"))
    hashmap.remove("key1")
    print(hashmap.get("key1"))