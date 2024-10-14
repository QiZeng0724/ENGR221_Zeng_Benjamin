"""
Benjamin Zeng
File Name: doublyLinked.py
Description: 
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self):
        return self.getFirstNode() is None

    def first(self):
        if self.isEmpty():
            raise Exception("List is empty")
        return self.getFirstNode().getValue()
    
    def getFirstNode(self):
        return self.__firstNode

    def getLastNode(self):
        return self.__lastNode
    
    def setFirstNode(self, node):
        if node != None and type(node) != DoubleNode:
            raise Exception("Input must be a valid Node or None")
        self.__firstNode = node

    def setLastNode(self, node):
        if node != None and type(node) != DoubleNode:
            raise Exception("Input must be a valid Node or None")
        self.__lastNode = node

    def find(self, value) -> DoubleNode:
        node = self.getFirstNode()
        while node != None:
            if node.getValue() == value:
                return node
            node = node.getNextNode()
        return None

    def insertFront(self, value):
        new_node = DoubleNode(value, self.getFirstNode())
        if self.isEmpty():
            self.setLastNode(new_node)
        else:
            self.getFirstNode().setPreviousNode(new_node)
        self.setFirstNode(new_node)

    def insertBack(self, value):
        new_node = DoubleNode(value, None, self.getLastNode())
        if self.isEmpty():
            self.setFirstNode(new_node)
        else:
            self.getLastNode().setNextNode(new_node)
        self.setLastNode(new_node)

    def insertAfter(self, value_to_add, after_value):
        node = self.find(after_value)
        if node == None:
            return False
        new_node = DoubleNode(value_to_add, node.getNextNode(), node)
        if node.getNextNode() != None:
            node.getNextNode().setPreviousNode(new_node)
        node.setNextNode(new_node)
        if new_node.getNextNode() == None:
            self.setLastNode(new_node)
        return True
    
    def deleteFirstNode(self):
        if self.isEmpty():
            raise Exception("List is empty")
        first = self.getFirstNode()
        self.setFirstNode(first.getNextNode())
        if self.getFirstNode() != None:
            self.getFirstNode().setPreviousNode(None)
        else:
            self.setLastNode(None)
        return first.getValue()
    
    def deleteLastNode(self):
        if self.isEmpty():
            raise Exception("List is empty")
        last = self.getLastNode()
        if self.getLastNode() == self.getFirstNode():
            self.setFirstNode(None)
            self.setLastNode(None)
        else:
            self.setLastNode(last.getPreviousNode())
            self.getLastNode().setNextNode(None)
        return last.getValue()
    
    def deleteValue(self, value):
        if self.isEmpty():
            raise Exception("List is empty; cannot delete")
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
            current = current.getNextNode()
        raise Exception("Value not found")

    def forwardTraverse(self):
        node = self.getLastNode()
        while node != None:
            print(node.getValue())
            node = node.getPreviousNode()

    def reverseTraverse(self):
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
    
    def __str__(self):
        out = "["
        node = self.getFirstNode()
        while node != None:
            if len(out) > 1:
                out += " <-> "
            out += str(node)
            node = node.getNextNode()
        return out + "]"
    
if __name__ == "__main__":
    pass