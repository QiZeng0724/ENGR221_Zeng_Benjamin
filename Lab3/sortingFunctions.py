"""
Name: Benjamin Zeng 
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> list: #sort "list_to_sort" using insertionSort.
    ### Interate each index over "list_to_sort" starting from the second element.
    for i in range(1, len(list_to_sort)):
        j = i
        ### While j is greater than 0 and "list_to_sort[j - 1]" is greater than "list_to_sort[j]".
        while j > 0 and list_to_sort[j - 1] > list_to_sort[j]:
            list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j] #swap "list_to_sort[j]" and "list_to_sort[j - 1]".
            j -= 1 #decrement j and continue comparing the elements.
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> list: #sort "list_to_sort" using bubbleSort.
    ### set n equal to the length of "list_to_sort".
    n = len(list_to_sort) 
    for i in range(n - 1): #iterate over index i from 0 to the length of "list_to_sort" - 1.
        for j in range(n - 1 - i): #iterate over index j from 0 to the length of "list_to_sort" - 1.
            if list_to_sort[j] > list_to_sort[j + 1]: #if "list_to_sort[j - 1]" is greater than "list_to_sort[j]".
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j] #swap "list_to_sort[j]" and "list_to_sort[j - 1]". 
    return list_to_sort

# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':
    pass