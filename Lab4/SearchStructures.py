"""
Name: Benjamin Zeng
SearchStructures.py
Description: Using stack and queue to search through a list.
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.__items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
        
    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.__items.append(item)

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        if not self.isEmpty():
            return self.__items.pop()
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.__items.append(item)

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        if not self.isEmpty():
            return self.__items.pop(0)
    
    