import pytest

from box import Box

def test_add():
    box = Box()
    
    #tests adding nicknames
    assert box.add("Rio", "Ampharos") == True #add a new nickname
    assert box.add("Hycan", "Ceruledge") == True #add nother nickname

    #tests adding a duplicate nickname
    assert box.add("Hycan","Armorouge") == False #tries to add an exsisting nickname

def test_find():
    box = Box()
    
    #adding nicknames
    assert box.add("Rio", "Ampharos") 
    assert box.add("Hycan", "Ceruledge") 

    #finding an exsisting entry with correct nickname
    entry = box.find("Rio", "Ampharos")
    assert entry is not None # should return entry
    assert entry.get_species() == "Ampharos" #should match the name of the species

    #finding an exsisting entry with incorrect species
    entry = box.find("Rio", "Ceruledge") 
    assert entry is None #should return none as species does not match with nickname

    #finding a non exsisting entry 
    entry = box.find("Hibi", "Ampharos")
    assert entry is None #should returm none as that is not the associated nickname 


def test_find_entry_by_nickname():
    box = Box()

    #adding nicknames
    assert box.add("Rio", "Ampharos") == True
    assert box.add("Hycan", "Ceruledge") == True

    #finding an exsisting entry
    entry = box.findEntryByNickname("Rio")
    assert entry is not None #should return entry
    assert entry.get_species() == "Ampharos" # nickname should match species

    #finding a non exsisting entry
    entry = box.findEntryByNickname("Hibi")
    assert entry is  None #should return none as nickname does not exsist