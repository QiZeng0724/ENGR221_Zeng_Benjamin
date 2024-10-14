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
        #Checks if the node is the first node in the list
        #Returns True if the node is the first node, else False
        
    def isLast(self) -> bool:
        return self.__nextNode == None
        #Checks if the node is the last node in the list
        #Return True if node is the last node, else False

    #####
    # Getters
    #####

    def getValue(self):
        return self.__value
        #Returns the value stored in the node
    
    def getNextNode(self):
        return self.__nextNode
        #Returns the next node in the list

    def getPreviousNode(self):
        return self.__previousNode
        #Returns the previous node in the list

    #####
    # Setters
    #####

    def setValue(self, new_value) -> None:
        self.__value = new_value
        #Sets a new value for the node

    def setNextNode(self, new_next) -> None:
        #Sets a new next node for the node
        if self.__checkValidNode(new_next):
            self.__nextNode = new_next
            #new_next = The new next node to be set

    def setPreviousNode(self, new_previous) -> None:
        #Sets a new previous node for the node
        if self.__checkValidNode(new_previous):
            self.__previousNode = new_previous
            #new_previous = The new previous node to be set
    #####
    # Helpers
    #####

    def __checkValidNode(self, node) -> bool:
        #Checks if a node is a valid DoubleNode or None
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
        #Returns True if the node is valid, else False
    
    def __str__(self):
        return str(self.getValue())
        #Returns a string representation of the node

if __name__ == "__main__":
    pass
