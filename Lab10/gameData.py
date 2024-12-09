"""
Author: Benjamin Zeng
File Name: gameData.py
Description: File to retain the snake's current datas.
"""

from boardCell import BoardCell
from preferences import Preferences

import random
from enum import Enum, auto


class GameData:
    def __init__(self):
        # Dimensions of the board (in cells)
        self.__height = Preferences.NUM_CELLS_TALL
        self.__width = Preferences.NUM_CELLS_WIDE

        # Keep track of how many cells are empty and in the board
        self.__freeCells = self.__height * self.__width
        self.__totalCells = self.__height * self.__width

        # The current movement mode of the snake (i.e., the current
        # direction or in AI mode
        self.__currentMode = self.SnakeMode.GOING_EAST

        #A 2D array of cells in the board
        self.__board = self.createBoard()

        #Score board starts at zero
        self.__score = 0

        # A list of cells that currently contain food (from oldest to newest)
        self.__foodCells = [] 
        # A list of cells that contain the snake (from head to tail)
        self.__snakeCells = []

        # Whether or not AI mode is on or off
        self.__aiMode = False

        # Whether or not the game is over
        self.__gameOver = False

    ##########################
    # Initialization methods #
    ##########################

    def getScore(self):
            """Return the current score."""
            return self.__score

    def increaseScore(self, amount=1):
            """Increase the score by a specified amount (default is 1)."""
            self.__score += amount

    def createBoard(self):
        """ Populate the starting state of the board.
            Returns a 2D array of cells in the board. """
        
        # Fill in the board with empty cells.
        board = [[BoardCell(row, col) for col in range(self.__width)] 
                                        for row in range(self.__height)]
        # Change the left and right edges to walls
        for row in range(self.__height):
            board[row][0].becomeWall()
            board[row][self.__width-1].becomeWall() 
            # Make sure these cells are not counted as "free"
            self.__freeCells -= 2
        # Change the top and bottom edges to walls
        for col in range(1, self.__width-1):
            board[0][col].becomeWall()
            board[self.__height-1][col].becomeWall()
            # Make sure these cells are not counted as "free"
            self.__freeCells -= 2

        return board
        
    def placeSnakeAtStartLocation(self):
        """ Place the snake in the upper left corner, facing east """

        head = self.getCell(1, 2)
        body = self.getCell(1, 1)
        
        # Mark these cells as the head and body
        head.becomeHead()
        body.becomeBody()

        # Add these cells to the snake cells list
        self.__snakeCells.append(head)
        self.__snakeCells.append(body)

        # Set the starting direction of the snake as east
        self.__currentMode = self.SnakeMode.GOING_EAST

        # Make sure these cells are not counted as "free"
        self.__freeCells -= 2

    ###############################
    # Information about the board #
    ###############################

    def inAIMode(self):
        """ Returns a boolean indicating whether or not we are in AI mode """
        return self.__currentMode == self.SnakeMode.AI_MODE

    def toggleAIMode(self):
        """Toggle the AI mode state."""
        self.__aiMode = not self.__aiMode

    def getCell(self, row, col):
        """ Returns the cell at the given row and column.
            Inputs: row - The row to get (between 0 and height-1)
                    col - The column to get (between 0 and width-1)
            Returns: The cell in that location """
        if (row >= 0 and row < self.__height) and (col >= 0 and col < self.__width):
            return self.__board[row][col]
        else:
            raise Exception("getCell tried to access cell outside of board: ({}, {})".format(row, col))
        
    def getNumRows(self):
        """Returns the number of rows in the board."""
        return self.__height

    def getNumCols(self):
        """Returns the number of columns in the board."""
        return self.__width

        
    ########################
    # Food related methods #
    ########################

    def noFood(self):
        """ Returns a boolean indicating whether 
            or not there is food on the board """
        return len(self.__foodCells) == 0
    
    def addFood(self):
        """ Adds food to an open spont on the board """

        # Find a value between 1 and self.__height-1 (inclusive)
        row = random.randrange(1, self.__height)
        # Find a value between 1 and self.__width-1 (inclusive)
        col = random.randrange(1, self.__width)
        # Get the cell at that location
        cell = self.getCell(row, col)

        # If it is empty, add food
        if cell.isEmpty():
            cell.becomeFood()
            self.__foodCells.append(cell)
            self.__freeCells -= 1

        # Otherwise, only add food if over 30% of our cells are free
        elif self.__freeCells / self.__totalCells > 0.3:
            self.addFood()

        # Otherwise, there is too much food on the board already
        else:
            print("Not adding more food")

    ##########################
    # Snake movement methods #
    ##########################

    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """

        print(f"Advancing snake to cell: {nextCell}")

        # If we run into a wall or the snake, it's game over
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()

        # If the snake eats food
        elif nextCell.isFood():
            print("Eating food")
            self.__data.eatFood(nextCell)
            nextCell.becomeHead()
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)

        # If the snake moves to an empty cell
        elif nextCell.isEmpty():
            print("Moving to empty cell")
            nextCell.becomeHead()
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)

            # Remove the tail
            tail = self.__data.removeTail()
            tail.becomeEmpty()

    ###############################
    # Methods to access neighbors #
    ###############################

    def getNorthNeighbor(self, cell):
        """ Returns the cell to the north of the given cell """
        return self.getCell(cell.getRow() - 1, cell.getCol())

        
    def getSouthNeighbor(self, cell):
        """Returns the cell to the south of the given cell """
        return self.getCell(cell.getRow() + 1, cell.getCol())

    def getEastNeighbor(self, cell):
        """ Returns the cell to the east of the given cell """
        return self.getCell(cell.getRow(), cell.getCol() + 1)

    def getWestNeighbor(self, cell):
        """ Returns the cell to the west of the given cell """
        return self.getCell(cell.getRow(), cell.getCol() - 1)
    
    def getHeadNorthNeighbor(self):
        """ Returns the cell to the north of the snake's head """
        return self.getNorthNeighbor(self.getSnakeHead())
    
    def getHeadSouthNeighbor(self):
        """ Returns the cell to the south of the snake's head """
        return self.getSouthNeighbor(self.getSnakeHead())
    
    def getHeadEastNeighbor(self):
        """ Returns the cell to the east of the snake's head """
        return self.getEastNeighbor(self.getSnakeHead())
    
    def getHeadWestNeighbor(self):
        """ Returns the cell to the west of the snake's head """
        return self.getWestNeighbor(self.getSnakeHead())
    
    def getNextCellInDir(self):
        """ Returns the next cell in the snake's path based
            on its current direction (self.__currentMode). """
    
        head = self.getSnakeHead()
        if self.__currentMode == self.SnakeMode.GOING_NORTH:
            return self.getNorthNeighbor(head)
        elif self.__currentMode == self.SnakeMode.GOING_SOUTH:
            return self.getSouthNeighbor(head)
        elif self.__currentMode == self.SnakeMode.GOING_EAST:
            return self.getEastNeighbor(head)
        elif self.__currentMode == self.SnakeMode.GOING_WEST:
            return self.getWestNeighbor(head)
        else:
            raise Exception("Invalid snake mode: {}".format(self.__currentMode))


    def getNeighbors(self, center):
        """ Returns a set of the neighbors around the given cell """
        return {self.getNorthNeighbor(center),
                self.getSouthNeighbor(center),
                self.getEastNeighbor(center),
                self.getWestNeighbor(center)}
    
    def getRandomNeighbor(self, center):
        """ Returns a random empty neighbor of the given cell """
        neighbors = self.getNeighbors(center)
        for cell in neighbors:
            if cell.isEmpty():
                return cell 
        # If none of them are empty, just return the first one
        return random.choice(neighbors)
    
    ###################################
    # Methods to set the snake's mode #
    ###################################
    
    def setDirectionNorth(self):
        """ Set the direction as north """
        self.__currentMode = self.SnakeMode.GOING_NORTH

    def setDirectionSouth(self):
        """ Set the direction as south """
        self.__currentMode = self.SnakeMode.GOING_SOUTH 

    def setDirectionEast(self):
        """ Set the direction as east """
        self.__currentMode = self.SnakeMode.GOING_EAST

    def setDirectionWest(self):
        """ Set the direction as west """
        self.__currentMode = self.SnakeMode.GOING_WEST

    def setAIMode(self):
        """ Switch to AI mode """
        self.__currentMode = self.SnakeMode.AI_MODE

    ###############################
    # Methods to access the snake #
    ###############################

    def getSnakeHead(self):
        """ Return the cell containing the snake's head """
        return self.__snakeCells[0]
    
    def getSnakeTail(self):
        """ Return the cell containing the snake's tail """
        return self.__snakeCells[-1]
    
    def getSnakeNeck(self):
        """ Return the body cell adjacent to the snake's head """
        return self.__snakeCells[1]

    #################################
    # Helper method for the display #
    #################################
    
    def getCellColor(self, row, col):
        """ Returns the color of the cell at the given location.
            Inputs: row - The row of the cell to access
                    col - The column of the cell to access """
        return self.getCell(row, col).getCellColor()
    
    ################################
    # Helper method(s) for reverse #
    ################################
    
    def reverseSnakeCells(self):
        """ Reverses the order of the snake cells. """
        self.__snakeCells.reverse()
        # Update head and tail references
        self.__snakeHead = self.__snakeCells[0]
        self.__snakeTail = self.__snakeCells[-1]
    
    def getSecondCell(self):
        """ Second scell of the snake returns. """
        if len(self.__snakeCells) > 1:
            return self.__snakeCells[1]
        raise ValueError("Snake does not have a second cell.")

    def addHead(self, cell):
        """ Adds a new head cell to the snake """
        self.__snakeCells.insert(0, cell)

    def removeTail(self):
        """ Removes the tail cell of the snake """
        return self.__snakeCells.pop()

    def eatFood(self, cell):
        """ Handles the logic when the snake eats food """
        self.__foodCells.remove(cell)  # Remove food from the food list
        self.__freeCells -= 1         # Update the free cell count


    #################################
    # Methods for AI implementation #
    #################################

    def inAIMode(self):
        return self.__aiMode

    def toggleAIMode(self):
        self.__aiMode = not self.__aiMode


    def resetCellsForSearch(self):
        for row in self.__board:
            for cell in row:
                cell.clearSearchInfo()
    
    #########################
    # Methods for Game over #
    #########################

    def setGameOver(self):
        """ Set the game over flag to True """
        self.__gameOver = True 

    def getGameOver(self):
        """ Check the game over value """
        return self.__gameOver
    
    ######################################
    # Helpers for printing and debugging #
    ######################################

    def __str__(self):
        """ Returns a string representation of the board """
        out = ""
        for row in self.__board:
            for cell in row:
                out += str(cell)
            out += "\n"
        return out
    
    def toStringParents(self):
        """ Returns a string representation of the parents of each cell """
        out = ""
        for row in self.__board:
            for cell in row:
                out += "{}\t".format(cell.parentString())
            out += "\n"
        return out

    class SnakeMode(Enum):
        """ An enumeration (or enum) to represent the valid
            SnakeModes, in order to ensure that we do not accidentally
            use an invalid mode. The auto() is used when the value of
            the objects does not matter.
        """
        GOING_NORTH = auto()
        GOING_SOUTH = auto()
        GOING_EAST = auto()
        GOING_WEST = auto()
        AI_MODE = auto()