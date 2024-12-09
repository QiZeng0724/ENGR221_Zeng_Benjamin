"""
Author: Benjamin Zeng
File Name: controller.py
Description: Controls the snake with assigned movement key.
"""

from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue

class Controller():
    def __init__(self):
        # The current state of the board
        self.__data = GameData()
        # The display
        self.__display = BoardDisplay()
        # How many frames have passed
        self.__numCycles = 0

        # Attempt to load any sounds and images
        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None

        # Initialize the board for a new game
        self.startNewGame()
        
    def startNewGame(self):
        """ Initializes the board for a new game """

        # Place the snake on the board
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """

        # Keep track of the time that's passed in the game 
        clock = pygame.time.Clock()

        # Loop until the game ends
        while not self.__data.getGameOver():
            # Run the main behavior
            self.cycle() 
            # Sleep
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self):
        """ The main behavior of each time step """

        # Check for user input
        self.checkKeypress()
        # Update the snake state
        self.updateSnake()
        # Update the food state
        self.updateFood()
        # Increment the number of cycles
        self.__numCycles += 1
        # Update the display based on the new state
        self.__display.updateGraphics(self.__data)

    def checkKeypress(self):
        """ Update the game based on user input """
        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.gameOver()
            # Change the snake's direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                # Reverse direction of snake
                if event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()
                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()
                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()
                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()
                elif event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()
                elif event.key in self.Keypress.AI.value:
                    self.__data.toggleAIMode()


    def updateSnake(self):
        """ Move the snake forward one step, either in the current 
            direction, or as directed by the AI """

        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            try:
                # Find the next cell
                if self.__data.inAIMode():
                    nextCell = self.getNextCellFromBFS()
                else:
                    nextCell = self.__data.getNextCellInDir()
                self.advanceSnake(nextCell)       
            except Exception as e:
                print(f"Failed to advance snake: {e}")
                nextCell = None
        else:
            nextCell = None
            print(f"Next cell: {nextCell}")
            # Move the snake to the next cell
            self.advanceSnake(nextCell)

        


    def advanceSnake(self, nextCell):
        """Update the world to move the snake's head to the given cell."""
    
        print(f"Advancing snake to cell: {nextCell}")

        # If the snake runs into itself or into a wall.
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()
        # If the snake eats foodCell.
        elif nextCell.isFood():
            self.__data.eatFood(nextCell)
            self.__data.increaseScore(amount=1)  # increase score by eating food
            nextCell.becomeHead()
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)

        # If the snake moves to an empty cell.
        elif nextCell.isEmpty():
            nextCell.becomeHead()
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)

            # Remove the tail.
            tail = self.__data.removeTail()
            tail.becomeEmpty()      

    def updateFood(self):
        """ Adds foodCell every cycle or if there is no foodCell on the board."""
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """Uses BFS to search for the food closest to the head of the snake."""
        """Returns the next step the snake should take along the shortest path to the closest food cell."""
        
        try:
        # Prepare all the tiles to search.
            self.__data.resetCellsForSearch()

            # Initialize a queue to hold the tiles to search.
            cellsToSearch = Queue()

            # Add the head to the queue and mark it as added.
            head = self.__data.getSnakeHead()
            head.setAddedToSearchList()
            cellsToSearch.put(head)

            while not cellsToSearch.empty():
                current = cellsToSearch.get()

                # Check if we found food.
                if current.isFood():
                    return self.getFirstCellInPath(current)

                # Add neighbors to the search.
                for neighbor in self.__data.getNeighbors(current):
                    if not neighbor.alreadyAddedToSearchList() and not neighbor.isWall() and not neighbor.isBody():
                        neighbor.setAddedToSearchList()
                        neighbor.setParent(current)
                        cellsToSearch.put(neighbor)

            # If the search failed, return a random neighbor.
            return self.__data.getRandomNeighbor(head)
    
        except Exception as e:
            print(f"BFS Error: {e}")
            raise

    def getFirstCellInPath(self, foodCell):
        """Trace back from the foodCell to the snake's head."""
        current = foodCell
        while current.getParent():  # Keep moving up the path until we reach the head
            if current.getParent() == self.__data.getSnakeHead():
                return current  # Return the cell immediately after the head
            current = current.getParent()
        return foodCell  

    
    def reverseSnake(self):
        """Reverses the snake's head and tail."""
        # Reverse the snake body cells
        self.__data.reverseSnakeCells()

        # Update the direction based on the new head and new second cell
        head = self.__data.getSnakeHead()
        try:
            second_cell = self.__data.getSecondCell()

            if head.getRow() > second_cell.getRow():  # When head is below the second cell
                self.__data.setDirectionNorth()
            elif head.getRow() < second_cell.getRow():  # When head is above the second cell
                self.__data.setDirectionSouth()
            elif head.getCol() > second_cell.getCol():  # When head is to the right of the second cell
                self.__data.setDirectionWest()
            elif head.getCol() < second_cell.getCol():  # When head is to the left of the second cell
                self.__data.setDirectionEast()
        except ValueError:
            print("Cannot reverse a snake with no second cell.")
        pass

    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ An enumeration (enum) defining the valid keyboard inputs 
            to ensure that we do not accidentally assign an invalid value.
        """
        UP = pygame.K_i, pygame.K_UP        # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN    # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT    # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT  # l and right arrow key
        REVERSE = pygame.K_r,               # r
        AI = pygame.K_a,                    # a


if __name__ == "__main__":
    Controller().run()