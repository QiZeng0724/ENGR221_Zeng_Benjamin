class MySet:
    # Constructor
    def __init__(self, initialValues = []):
        self.__s = []   # List to store the set values
        self.__setsize = 0  # Tracks the size of the set

        # Add only unique values to the set
        for value in initialValues:
            if value not in self.__s:
                self.__s.append(value)
                self.__setsize += 1

    # Search for a value in the set
    def search(self, value):
        for item in self.__s:
            if item == value:
                return True  # Value found
        return False  # Value not found

    # Insert a new value into the set
    def insert(self, value):
        if value not in self.__s:
            self.__s.append(value)
            self.__setsize += 1

    # Delete a value from the set
    def delete(self, value):
        if value in self.__s:
            self.__s.remove(value)
            self.__space -= 1
            return True  # Successfully deleted
        return False  # Value not found

    # Traverse and print all values in the set
    def traverse(self):
        for item in self.__s:
            print(item)

    # Return the size of the set
    def size(self):
        return self.__size

    # Return the list of values in the set
    def vals(self):
        return self.__s

# Example usage:
if __name__ == '__main__':
    pass
