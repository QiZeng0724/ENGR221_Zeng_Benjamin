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
                if event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()
                # Enter AI mode
                elif event.key in self.Keypress.AI.value:
                    self.__data.setAIMode()
                # Change directions
                # TODO fill in to change snake direction
                elif event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()
                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()
                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()
                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()
                

    def updateSnake(self):
        """ Move the snake forward one step, either in the current 
            direction, or as directed by the AI """

        # Move the snake once every REFRESH_RATE cycles
        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            try:
            # Find the next place the snake should move
                if self.__data.inAIMode():
                    nextCell = self.getNextCellFromBFS()
                else:
                    nextCell = self.__data.getNextCellInDir()
            except Exception as e:
                print(f"Failed to advance Snake: {e}")
            print(f"Next cell: {nextCell}")
            self.advanceSnake(nextCell)


    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """

        # If we run into a wall or the snake, it's game over
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()
        
        # If we eat food, update the state of the board
        elif nextCell.isFood():
            self.__data.eatFood(nextCell)
            nextCell.becomeHead()
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)
            
        # TODO Possibly add code here, using the helper methods
        elif nextCell.isEmpty():
            nextCell.becomeHead()
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)

            tail = self.__data.removeTail()
            tail.becomeEmpty()
        # in gameData.py under the "snake movement methods" header

    def updateFood(self):
        """ Add food every FOOD_ADD_RATE cycles or if there is no food """
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """ Uses BFS to search for the food closest to the head of the snake.
            Returns the *next* step the snake should take along the shortest path
            to the closest food cell. """
        
        # Parepare all the tiles to search
        self.__data.resetCellsForSearch()

        # Initialize a queue to hold the tiles to search
        cellsToSearch = Queue()

        # Add the head to the queue and mark it as added
        head = self.__data.getSnakeHead()
        head.setAddedToSearchList()
        cellsToSearch.put(head)

        # Search!
        # TODO implement BFS here

        # If the search failed, return a random neighbor
        return self.__data.getRandomNeighbor(head)

    def getFirstCellInPath(self, foodCell):
        """ TODO COMMENT HERE """

        # TODO
        
        return foodCell
    
    def reverseSnake(self):
        """ TODO COMMENT HERE """

        # TODO

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