"""
Name: Benjamin Zeng
File name: box.py
Desciption: Implementing and testing methods in the box class
"""
from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='Lab7/entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):
        if self.nicknameMap.containsKey(nickname): #if nickname exsists in the box
            return False #return false as it is already in the box
        else:# if nickname is not in the box
            entry = Entry(nickname,species) #creates an entry object
            self.nicknameMap.put(nickname, entry) #adds the entry object to the nickname map
            return True #returns true to indicate that entry is sucessfully added
    
    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        if self.nicknameMap.containsKey(nickname): #checks if given nickname exsists in the map
            entry = self.nicknameMap.get(nickname) #get the entry associated with the nickname

            compEntry = Entry(nickname,species) #creates a comparison entry object

            if entry.get_species() ==  compEntry.get_species():#if species matches between entries
                return entry # returns entry if species matches
            
        return None #return none if species does not match  or nickname does not exsist 
    
    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    def findAllNicknames(self):
        return self.nicknameMap.keys() #returns a list of all unique nicknames (empty list if box is empty)

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        if self.nicknameMap.containsKey(nickname): #checks if given nickname exsists in the map
            return self.nicknameMap.get(nickname) #returns the Entry with the given nickname
    
        return None #returns an empty list

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        if self.nicknameMap.containsKey(nickname): #checks if given nickname exsists in the map
            self.nicknameMap.remove(nickname) #returns the Entry with the given nickname
            return True #returns true if nickname was succersfully removed
        
        return False #returns false if nickname was unsuccersfully removed

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        if not self.nicknameMap.containsKey(nickname): #checks if given nickname is in the map
            return False # returns false if nickname is not found
        
        entry = self.nicknameMap.get(nickname)#gets entry that is associated with the nickname 

        #checks if specices macthes specified species
        if entry.get_species() == species:
            self.nicknameMap.remove(nickname) #removes entry from map
            return True #returns true if sucessfully removed
        
        return False #returns true if species does not match/exsist

if __name__ == '__main__':
    pass