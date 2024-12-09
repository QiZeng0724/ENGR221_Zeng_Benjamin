"""
Author: Benjamin Zeng
File Name: preferences.py
Description: Preferences/settings the player can modify.
"""

import pygame

class Preferences:
    pygame.init()


    ##########
    # Timing #
    ##########

    # How frequently to move the snake
    REFRESH_RATE = 1
    # How frequently to add food to the board
    FOOD_ADD_RATE = 25    
    # How long to sleep between updates
    SLEEP_TIME = 15

    ##########
    # Sizing #
    ##########

    # Dimensions of the board
    NUM_CELLS_WIDE = 50
    NUM_CELLS_TALL = 30

    # Size of each cell in pixels
    CELL_SIZE = 20

    # Dimensions of the board in pixels
    GAME_BOARD_WIDTH = NUM_CELLS_WIDE * CELL_SIZE
    GAME_BOARD_HEIGHT = NUM_CELLS_TALL * CELL_SIZE

    ##########
    # Colors #
    ##########

    COLOR_BACKGROUND = pygame.Color('lavender')
    COLOR_WALL = pygame.Color('gray40')
    COLOR_FOOD = pygame.Color('darkgoldenrod1')
    COLOR_EMPTY = pygame.Color('lavender')
    COLOR_HEAD = pygame.Color('aquamarine3')
    COLOR_BODY = pygame.Color('aquamarine3')

    ##########################
    # Game over text display #
    ##########################
    
    GAME_OVER_X = GAME_BOARD_HEIGHT / 2
    GAME_OVER_Y = GAME_BOARD_WIDTH / 2
    GAME_OVER_COLOR = pygame.Color('gray0')
    GAME_OVER_FONT = pygame.font.SysFont("arial", 80)
    GAME_OVER_TEXT = "YOU LOSE!!"

    ######################
    # Graphics and Audio #
    ######################

    # Image to display as the head
    HEAD_IMAGE = "Lab10/trainer.png"
    # Sound to play when eating
    EAT_SOUND = "meow.wav"

    SCORE_COLOR = (0, 0, 0)  # Black