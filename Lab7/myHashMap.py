"""
Name: Benjamin Zeng
File name: myHashMap.py
Description: Impletmenting and testing methods in MyHashMap class
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
            for entry in bucket:
                index = hash(entry.getKey()) % self.capacity
                new_buckets[index].append(entry)
        # Update the self.buckets attribute with the new entries
        self.buckets = new_buckets

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        #if the key is None
        if key is None:
            raise Exception("None is not a valid key") # raises an exception

        #if adding a new key would surpass the load factor
        if self.size / self.capacity >= self.load_factor:
            self.resize() #resizes the capacity of MyHashMap

        index = hash(key) % self.capacity #calculates the bucket index for the key value pairs based on hash(key)

        #Checks if key is in the bucket
        for entry in self.buckets[index]:
            if entry.getKey() == key: #if the key is found
                entry.setValue(value) #updates the value of the exsisting key 
                return False #returns false as there was no new key to add
        
        newEntry = self.MyHashMapEntry(key, value) #creates a new entry 
        self.buckets[index].append(newEntry) #adds the new entry to the appropriate bucket 
        self.size += 1 #incraments the size of the hash map 
        return True #returns true if the key is sucessfully added to the has map

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """

    def replace(self, key, newValue):
        #if the key is None
        if key is None:
            raise Exception("None is not a valid key") # raises an exception

        index = hash(key) % self.capacity #calculates the bucket index for the key value pairs based on hash(key)

        #iterates over every entry in self bucket's index
        for entry in self.buckets[index]: 
            if entry.getKey() == key: #if key is in the hashmap
               entry.setValue(newValue) #replaces the key
               return True #returns true as key is in the hashamp aand was sucessfully replaced 
            
        return False #returns false as no key is replaced 
    
    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        #if the key is None
        if key is None:
            raise Exception("None is not a valid key") # raises an exception

        index = hash(key) % self.capacity #calculates the bucket index for the key value pairs based on hash(key)
        #iterates over every entry in self bucket's index
        for entry in self.buckets[index]: 
            if entry.getKey() == key: #if the value from get key matches key
               self.buckets[index].remove(entry) #removes the key 
               self.size -= 1 #decrements by one
               return True #key was sucessfully removed
            
        return False #key was not in the hashmap
    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        #if the key is None
        if key is None:
            raise Exception("None is not a valid key") # raises an exception

        index = hash(key) % self.capacity #calculates the bucket index for the key value pairs based on hash(key)

        #iterates over every entry in self bucket's index
        for entry in self.buckets[index]:
            if entry.getKey() == key: #if the key is present in the hash map
                entry.setValue(value) #update the value of the exsiting key 
                return True #returns true to indicate that an update occured
        
        newEntry = self.MyHashMapEntry(key, value) #if key was not found
        self.buckets[index].append(newEntry) #append the new entry to the appropriate bucket
        self.size += 1 #incrament size of hash map
        return False #return false to indicate a new key value pair 

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        #if the key is None
        if key is None:
            raise Exception("None is not a valid key") # raises an exception

        index = hash(key) % self.capacity #calculates the bucket index for the key value pairs based on hash(key)
        
        #iterates over every entry in self bucket's index
        for entry in self.buckets[index]:
            if entry.getKey() == key: #if key matches the specified key
                return entry.getValue() #returns the value of the specified key
           
        return None #key is not in the hash map

    """
    Return the number of key, value pairs in this MyHashMap. """
    def get_size(self):
       return self.size #returns the size of the hashmap (# of key value pairs)

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        return self.size == 0  #returns true if hash map conatains no elements, false if otherwise

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        #if the key is None
        if key is None:
            raise Exception("None is not a valid key") # raises an exception

        index = hash(key) % self.capacity #calculates the bucket index for the key value pairs based on hash(key)

        #iterates over every entry in self bucket's index
        for entry in self.buckets[index]:
            if entry.getKey() == key: #if the specified key is in the hash map
                return True #returns true indiciating key is in the hash map
            
        return False #returns true indiciating key is not in the hash map

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        list =[] #initializes an empty list 

        #iterates over every bucket in selfbucket
        for bucket in self.buckets:
            for entry in bucket:  #iterates over every entry in bucket
                list.append(entry.getKey()) #appends the values of the keys 
            
        return list #rerturns a list with the keys of the hash map (empty list if it's empty)

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
   pass