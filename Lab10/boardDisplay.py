"""
Author: Benjamin Zeng
File Name: boardDisplay.py
Description: Displays and renders the graphics on the current state of the board.
"""

import pygame
from preferences import Preferences

class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode((Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT))
        # Image to show as the "head"
        self.headImage = pygame.image.load(Preferences.HEAD_IMAGE).convert_alpha()
        self.headImage = pygame.transform.scale(self.headImage, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))

        pygame.font.init()  # Initialize pygame font module
        self.__font = pygame.font.SysFont("Arial", 24)  # Set font and size

    def updateGraphics(self, gameData):
        """ Re-draws the board, food, and snake based
            on the current state of the board """
        
        # Clear the board
        self.clear()

        # Draw the board
        numRows = gameData.getNumRows()
        numCols = gameData.getNumCols()

        # Draw each cell on the board
        for row in range(numRows):
            for col in range(numCols):
                cell = gameData.getCell(row, col)  # Get the cell at (row, col)
                self.drawSquare(cell)             # Draw the cell based on its type

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()

        # Draw the score board
        self.displayScore(gameData)

        # Update the display
        pygame.display.update()
        
        # Update the display
        pygame.display.update()

    def clear(self):
        """ Resets the background of the display """
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell):#row, col, cellColor):
        """ Draws a cell-sized square at the given location.
            Inputs: row - row coordinate of the square to draw
                    col - column coordinate of the square to draw
                    cellColor - color of the square to draw """
        row = cell.getRow()
        col = cell.getCol()

        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
        else:
            cellColor = cell.getCellColor()
            pygame.draw.rect(self.__display, cellColor, [col*Preferences.CELL_SIZE, row*Preferences.CELL_SIZE, 
                                                     Preferences.CELL_SIZE, Preferences.CELL_SIZE])


    def drawImage(self, row, col, image):
        """ Displays an image at the given cell location.
            Inputs: row - row coordinate to draw the image at
                    col - column coordinate to draw the image at
                    image - the pygame image to draw """

        # First, convert the image to a Surface type (with transparent background)
        image = image.convert_alpha()
        # You will want to uncomment the below line if you want your image to fit within one cell
        #image = pygame.transform.scale(image, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))
        # Grab the dimensions of the image
        imageRect = image.get_rect()
        # Place the image in the center of the given cell coordinates
        imageRect.center = ((col*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
                            (row*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2))
        # Place the image on the display
        self.__display.blit(image, imageRect)

    def displayScore(self, gameData):
        """Displays the current score on the screen."""
        score_text = f"Score: {gameData.getScore()}"  # Format the score
        score_surface = self.__font.render(score_text, True, Preferences.SCORE_COLOR)  # Create text surface
        self.__display.blit(score_surface, (10, 10))  # Position the score board to the top-left corner

    def displayGameOver(self):
        """Displays the game over message."""
        # Get the font
        font = Preferences.GAME_OVER_FONT
        # Create the text
        text = font.render(Preferences.GAME_OVER_TEXT, True, Preferences.GAME_OVER_COLOR)
        # Get the dimensions of the text box
        textRect = text.get_rect()
        # Specify the location of the text
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)
        # Place the game over text on the display
        self.__display.blit(text, textRect)