"""Module that defines class for playing game of life."""

import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]])
blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]])
glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]])


class Game:

    """Class defining the game of life."""
    def __init__(game, size):
        """Initialises size of board."""
        game.board = np.zeros((size, size))

    def play(self):
        """Start the game."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Defines what a move does."""
        STENCIL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbour_count = convolve2d(self.board, STENCIL, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if (neighbour_count[i, j] == 3 or
                        (neighbour_count[i, j] == 2 and self.board[i, j])):
                    self.board = 1
                else:
                    self.board = 0

    def __setitem__(self, key, value):
        """Sets the value of a square on the board."""
        self.board[key] = value

    def show(self):
        """Prints out the game graphically."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()


class Pattern:

    """Class that generates patterns for the game of life"""
    def __init__(self, array):
        """Takes initial numpy array as pattern."""
        if not isinstance(array, np.ndarray):
            raise ValueError("Not a Numpy array!")
        self.grid = array

    def flip_vertical(self):
        """Takes a pattern and mirros along along x-axis."""
        return self.grid[::-1, :]

    def flip_horizontal(self):
        """Takes pattern and mirrors along y-axis."""
        return self.grid[:, ::-1]

    def flip_diag(self):
        """Transpose of the pattern."""
        return self.grid.T

    def rotate(self, n):
        """Rotates pattern n * 90 degrees."""
        if n % 4 == 0:
            return self.grid
        elif n % 4 == 1:
            rot90 = self.grid[:, ::-1]
            return rot90.T
        elif n % 4 == 2:
            rot180 = self.grid[:, ::-1]
            return rot180[::-1, :]
        else:
            rot270 = self.grid[::-1, :]
            return rot270.T
