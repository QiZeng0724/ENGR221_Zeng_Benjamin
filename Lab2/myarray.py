"""
Author: Benjamin Zeng
Filename: myarray.py
Description: Implementation of an unsorted array with duplicates
"""

class MyArray():
    # Constructor
    def __init__(self, initialSizeOrValues):
        if type(initialSizeOrValues) is int:
            self.__a = [None] * initialSizeOrValues # The array stored as a list
            self.__length = 0               # Start with no values in the list
            self.__space = initialSizeOrValues
        elif type(initialSizeOrValues) is list:
            self.__a = initialSizeOrValues
            self.__length = len(self.__a)
            self.__space = len(self.__a)
        
    # Return the current length of the array
    def length(self):
        return self.__length 
    
    # Return a list of the current array values
    def values(self):
        return self.__a[:self.__length]

    # Return the value at index idx
    # Otherwise, do not return anything
    def get(self, idx):
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         return self.__a[idx]              # only return item if in bounds
 
    # Set the value at index idx
    def set(self, idx, value):         
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         self.__a[idx] = value               # only set item if in bounds
    
    # Insert value to the end of the array
    def insert(self, value):
        if self.__length == self.__space:
            self.__space += 1
            self.__a.append(None)
        
        # Increment the length
        self.__a[self.__length] = value
        self.__length += 1   
    
    # Return the index of value in the array, 
    # or -1 if value is not in the array
    def search(self, value):

        # Only search the indices we've inserted
        for idx in range(self.__length): 

            # Check the value at the current index 
            if self.__a[idx] == value:  

                # Return the index  
                return idx  
            
        # Return -1 if value was not found             
        return -1                        

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        clearall = False

        while True:
            # Find the index of the value to delete
                idx = self.search(value)
                
                # If the value was found
                if idx != -1:
                    clearall = True

                    # Decrement the array length
                    self.__length -= 1

                    # Shift all the remaining values 
                    for j in range(idx, self.__length):
                        self.__a[j] = self.__a[j+1]
                    
                    self.__a[self.__length] = None
                else:
                    break
        # Return clearall if the value was not found
        return clearall
    
    # Print all items in the list
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])

if __name__ == '__main__':
    pass
