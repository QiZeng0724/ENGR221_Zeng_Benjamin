"""
Benjamin Zeng
File Name: doublyLinked.py
Description: Implementing efficient insertion and removal of elements at both ends of the list
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self):
        return self.getFirstNode() is None
        #Check if the list is empty, return True if it's empty, else False

    def first(self):
        if self.isEmpty():
            raise Exception("List is empty")
            # Raise exception if the list is empty
        return self.getFirstNode().getValue()
        #Returns the value of the first node in the list
    
    def getFirstNode(self):
        #Returns the value of the first node in the list
        return self.__firstNode

    def getLastNode(self):
        #Returns the value of the last node in the list
        return self.__lastNode
    
    def setFirstNode(self, node):
        #Sets the first node in the list
        if node != None and type(node) != DoubleNode:
            raise Exception("Input must be a valid Node or None")
            #Raise Exception if the input is not a valid DoubleNode or None
        self.__firstNode = node

    def setLastNode(self, node):
        #Sets the last node in the list
        if node != None and type(node) != DoubleNode:
            raise Exception("Input must be a valid Node or None")
            #Raise Exception if the input is not a valid DoubleNode or None
        self.__lastNode = node

    def find(self, value) -> DoubleNode:
        #Finds a node with a given value in the list.
        node = self.getFirstNode()
        while node != None:
            if node.getValue() == value:
                return node
            node = node.getNextNode()
        return None
        #Returns the node with the given value, or None if not found

    def insertFront(self, value):
        #Inserts a new node with a given value at the front of the list
        new_node = DoubleNode(value, self.getFirstNode())
        if self.isEmpty():
            self.setLastNode(new_node)
        else:
            self.getFirstNode().setPreviousNode(new_node)
        self.setFirstNode(new_node)

    def insertBack(self, value):
        #Inserts a new node with a given value at the back of the list
        new_node = DoubleNode(value, None, self.getLastNode())
        if self.isEmpty():
            self.setFirstNode(new_node)
        else:
            self.getLastNode().setNextNode(new_node)
        self.setLastNode(new_node)

    def insertAfter(self, value_to_add, after_value):
        #Inserts a new node with a given value after a node with a given value
        node = self.find(after_value)
        #The value of the node after which to insert
        if node == None:
            return False
        new_node = DoubleNode(value_to_add, node.getNextNode(), node)
        #The value to be inserted
        if node.getNextNode() != None:
            node.getNextNode().setPreviousNode(new_node)
        node.setNextNode(new_node)
        if new_node.getNextNode() == None:
            self.setLastNode(new_node)
        return True
        #Returns True if the insertion was successful, else False
    
    def deleteFirstNode(self):
        #Deletes the first node in the list
        if self.isEmpty():
            raise Exception("List is empty")
            #Raises Exception if the list is empty
        first = self.getFirstNode()
        self.setFirstNode(first.getNextNode())
        if self.getFirstNode() != None:
            self.getFirstNode().setPreviousNode(None)
        else:
            self.setLastNode(None)
        return first.getValue()
        #Return the value of the deleted node 
    
    def deleteLastNode(self):
        #Deletes the last node in the list
        if self.isEmpty():
            raise Exception("List is empty")
            #Raise Exception if the list is empty
        last = self.getLastNode()
        if self.getLastNode() == self.getFirstNode():
            self.setFirstNode(None)
            self.setLastNode(None)
        else:
            self.setLastNode(last.getPreviousNode())
            self.getLastNode().setNextNode(None)
        return last.getValue()
        #Return the value of the deleted node
    
    def deleteValue(self, value):
        #Deletes the first occurrence of a node with a given value in the list
        if self.isEmpty():
            raise Exception("List is empty; cannot delete")
            #Raises Exception if the list is empty
        current = self.getFirstNode()
        while current != None:
            if current.getValue() == value:
                if current.getPreviousNode() != None:
                    current.getPreviousNode().setNextNode(current.getNextNode())
                else:
                    self.setFirstNode(current.getNextNode())
                if current.getNextNode() != None:
                    current.getNextNode().setPreviousNode(current.getPreviousNode())
                else:
                    self.setLastNode(current.getPreviousNode())
                return current.getValue()
                #Returns the value of the deleted node
            current = current.getNextNode()
        raise Exception("Value not found")
        #Raises Exception if the value is not found

    def forwardTraverse(self):
        #Traverses the list from front to back and prints the values of the nodes
        node = self.getLastNode()
        while node != None:
            print(node.getValue())
            node = node.getPreviousNode()

    def reverseTraverse(self):
        #Traverses the list from back to front and prints the values of the nodes
        node = self.getLastNode()
        while node != None:
            print(node.getValue())
            node = node.getPreviousNode()

    def __len__(self):
        length = 0
        node = self.getFirstNode()
        while node != None:
            length += 1
            node = node.getNextNode()
        return length
        #Returns the number of nodes in the list
    
    def __str__(self):
        out = "["
        node = self.getFirstNode()
        while node != None:
            if len(out) > 1:
                out += " <-> "
            out += str(node)
            node = node.getNextNode()
        return out + "]"
        #Returns a string representation of the list
    
if __name__ == "__main__":
    pass
