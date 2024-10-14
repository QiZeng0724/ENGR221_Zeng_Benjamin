"""
Benjamin Zeng
File Name: doubleNode.py
Description: Creating a bi-directional node, which has a pointer to the previous node in the list.
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__nextNode = next
        self.__previousNode = previous 

    #####
    # Methods
    #####
        
    def isFirst(self) -> bool:
        return self.__previousNode == None
        
    def isLast(self) -> bool:
        return self.__nextNode == None

    #####
    # Getters
    #####

    def getValue(self):
        return self.__value
    
    def getNextNode(self):
        return self.__nextNode

    def getPreviousNode(self):
        return self.__previousNode

    #####
    # Setters
    #####

    def setValue(self, new_value) -> None:
        self.__value = new_value

    def setNextNode(self, new_next) -> None:
        if self.__checkValidNode(new_next):
            self.__nextNode = new_next

    def setPreviousNode(self, new_previous) -> None:
        if self.__checkValidNode(new_previous):
            self.__previousNode = new_previous

    #####
    # Helpers
    #####

    def __checkValidNode(self, node) -> bool:
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    def __str__(self):
        return str(self.getValue())

if __name__ == "__main__":
    pass