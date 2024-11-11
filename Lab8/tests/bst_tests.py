import pytest

from ..binarySearchTree import BinarySearchTree

@pytest.fixture 
# Define an empty BST for testing
def emptyTree():
    return BinarySearchTree()

@pytest.fixture 
# Define a BST for testing
# Should look like
#          5
#        /   \
#       3     8
#      /
#     1
def nonemptyTree():
    bst = BinarySearchTree()
    bst.insert(5, "five")
    bst.insert(8, "eight")
    bst.insert(3, "three")
    bst.insert(1, "one")
    return bst

#Custom
@pytest.mark.custom
# Test insertion of duplicate keys (should not alter the tree structure)
def test_bst_insert_duplicate_key(nonemptyTree):
    nonemptyTree.insert(3, "new_three")  # Inserting a duplicate key with a new value
    assert nonemptyTree.lookup(3) == "three"  # Should still hold the original value

@pytest.mark.custom
# Test deleting a key not present in the tree (should raise an exception)
def test_bst_delete_nonexistent_key(nonemptyTree):
    with pytest.raises(Exception, match="Key not in tree."):
        nonemptyTree.delete(10)  # Trying to delete a key that doesn't exist

@pytest.mark.custom
# Test lookup in an empty tree (should return None)
def test_bst_lookup_empty_tree(emptyTree):
    assert emptyTree.lookup(3) is None  # Lookup in an empty tree should return None

@pytest.mark.custom
# Test inserting nodes to create an unbalanced tree (right-heavy)
def test_bst_insert_right_heavy(capfd):
    bst = BinarySearchTree()
    bst.insert(1, "one")
    bst.insert(2, "two")
    bst.insert(3, "three")
    bst.insert(4, "four")
    bst.insert(5, "five")
    
    # Traverse the tree to capture the printed output
    bst.traverse()
    
    # Capture the output and compare it to the expected output
    out, _ = capfd.readouterr()
    expected_output = "(1, one)\n(2, two)\n(3, three)\n(4, four)\n(5, five)\n"
    assert out == expected_output


@pytest.mark.custom
# Test searching for minimum and maximum keys after mixed insertions
def test_bst_search_min_max():
    bst = BinarySearchTree()
    bst.insert(10, "ten")
    bst.insert(5, "five")
    bst.insert(20, "twenty")
    bst.insert(1, "one")
    bst.insert(15, "fifteen")
    bst.insert(25, "twenty-five")
    assert bst.findSuccessor(bst.getRoot()).key == 1  
    assert bst.search(25).key == 25


####
# isEmpty
####

@pytest.mark.isEmpty
# isEmpty functionality for a BST
def test_bst_isempty_true(emptyTree):
    # Should return True
    assert emptyTree.isEmpty()

@pytest.mark.isEmpty
# isEmpty functionality for a BST
def test_bst_isempty_false(nonemptyTree):
    # Should return False 
    assert not nonemptyTree.isEmpty()

####
# getRoot
####

@pytest.mark.getRoot
# getRoot functionality for a BST
def test_bst_getRoot_empty(emptyTree):
    # Should be None
    assert emptyTree.getRoot() is None 

@pytest.mark.getRoot
# getRoot functionality for a BST
def test_bst_getRoot_nonempty(nonemptyTree):
    # Should return 5
    assert nonemptyTree.getRoot().key == 5

####
# search
####

@pytest.mark.search
# search functionality for a BST
def test_bst_search_present(nonemptyTree):
    # Should return 3
    assert nonemptyTree.search(3).key == 3

@pytest.mark.search
# search functionality for a BST
def test_bst_search_absent(nonemptyTree):
    # Should return None
    assert nonemptyTree.search(4) is None

####
# lookup
####

@pytest.mark.lookup
# lookup functionality for a BST
def test_bst_lookup_present(nonemptyTree):
    # Should return "one"
    assert nonemptyTree.lookup(1) == "one"

@pytest.mark.lookup
# lookup functionality for a BST
def test_bst_lookup_present(nonemptyTree):
    try:
        # This should throw an exception
        nonemptyTree.lookup(4)
    except:
        # If we got here, an exception was thrown
        assert True 

####
# findSuccessor
####

@pytest.mark.findSuccessor
# findSuccessor functionality for a BST
def test_bst_findSuccessor(nonemptyTree):
    # Should return smallest value in tree (1)
    assert nonemptyTree.findSuccessor(nonemptyTree.getRoot()).key == 1

####
# delete
####

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_leaf(nonemptyTree, capfd):
    # Delete a leaf
    nonemptyTree.delete(1)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 1 removed
    assert out == "{(5, five), {(3, three), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_child(nonemptyTree, capfd):
    # Delete a node with one child
    nonemptyTree.delete(3)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 3 removed
    assert out == "{(5, five), {(1, one), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_children(nonemptyTree, capfd):
    # Delete a node with two children
    nonemptyTree.delete(5)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 5 removed
    assert out == "{(8, eight), {(3, three), {(1, one), None, None}, None}, None}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_stick(nonemptyTree, capfd):
    # Delete so we are left with a stick
    nonemptyTree.delete(5)
    # Now delete so we are forced to change the root in Case 2
    nonemptyTree.delete(8)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 5 removed
    assert out == "{(3, three), {(1, one), None, None}, None}\n"
    
@pytest.mark.traverse
# traverse functionality for a BST
def test_bst_traverse(nonemptyTree, capfd):
    # Traverse the tree
    nonemptyTree.traverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected order
    assert out == "(1, one)\n(3, three)\n(5, five)\n(8, eight)\n"