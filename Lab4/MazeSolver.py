"""
Name: Benjamin Zeng
MazeSolver.py
Description: Using stacks and queue to solve a maze
"""
from .SearchStructures import Stack, Queue
from .Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        # ~~~~~~~~
        # Write your tileIsVisitable() implementation here
        # ~~~~~~~~
        if 0 <= row < len(self.maze.contents) and 0 <= col < len(self.maze.contents[0]):
            tile = self.maze.contents[row][col]

            if not tile.isWall() and not tile.visited():
                return True
        return False

    def solve(self):
        # ~~~~~~~~
        # Write your solve() implementation here
        # ~~~~~~~~
        start = self.maze.start
        self.ss.add(start)
        
        while not self.ss.isEmpty():
            current = self.ss.remove()
            current.visit()

            if current == self.maze.goal:
                return current

     # Add any other helper functions you might want here
            else:
                for rowDirection, colsDirection in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow = current.getRow() + rowDirection
                    newCols = current.getCol() + colsDirection

                    if self.tileIsVisitable(newRow, newCols):
                        neighbor = self.maze.contents[newRow][newCols]
                        neighbor.setPrevious(current)
                        self.ss.add(neighbor)

    def getPath(self):
        # ~~~~~~~~
        # Write your getPath() implementation here
        # ~~~~~~~~
        path = []
        current = self.maze.goal

        while current is not None:
            path.append(current)
            current = current.getPrevious()
        
        path.reverse()
        return path

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##E",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()