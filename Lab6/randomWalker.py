"""
Benjamin Zeng
File name: randomWalker.py
Description: Simulating a walkway with boundary and radom steps.
Assignment adapted from HMC CS5
"""

import random  
import time

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!

def rwstepsLoop(start, low, hi):
    steps = 0
    while start > low and start < hi:          
        position = start + rs()                # Takes random step from position, returns 1 or -1
        start = position                       # Updates the position
        steps += 1

        walkway = "_" * (hi - low)
        S = start - low                        # Calculate the index of the walker's current position relative to the walkway

        walkway = walkway[:S] + "S" + walkway[S:]   # Insert the walker's marker ("S") into the walkway at the current position
        walkway = " " + walkway + " "

        print(walkway, "    ", start, low, hi)      # Print the current state of the walkway, the walker's position, and the boundaries
        time.sleep(0.05)
    return steps                                    # Return the total number of steps taken when the walker reaches an edge

if __name__ == '__main__':
    print(rs())