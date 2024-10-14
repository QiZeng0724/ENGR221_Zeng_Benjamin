"""
Benjamin Zeng
File Name: deque.py
Description: Implementing efficient insertion and removal of elements at both ends of the deque
"""

from .doublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    #Checks if the Deque is empty
    def isEmpty(self):
        return self.__values.isEmpty()
        #Returns True if the Deque is empty, False otherwise

    def __len__(self):
        return len(self.__values)
        #Returns the number of elements in the Deque
    
    def __str__(self):
        return str(self.__values)
        #Returns a string representation of the Deque
    
    def peekLeft(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
            #Raises Exception if the Deque is empty
        return self.__values.getFirstNode().getValue()
        #Returns the value of the leftmost element in the Deque
    
    def peekRight(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
            #Raises Exception if the Deque is empty
        return self.__values.getLastNode().getValue()
        #Returns the value of the rightmost element in the Deque

    def insertLeft(self, value):
        self.__values.insertFront(value)
        #Inserts a value at the left end of the Deque
        
    def insertRight(self, value): 
        self.__values.insertBack(value)
        #Inserts a value at the right end of the Deque

    def removeLeft(self): 
        if self.isEmpty():
            raise Exception("Deque is empty")
            #Raises Exception if the Deque is empty
        return self.__values.deleteFirstNode()
        #Removes and returns the value of the leftmost element in the Deque

    def removeRight(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
            #Raises Exception if the Deque is empty
        return self.__values.deleteLastNode()
        #Removes and returns the value of the rightmost element in the Deque
    
if __name__ == "__main__":
    pass
