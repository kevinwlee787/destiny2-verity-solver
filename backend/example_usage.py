import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'verity_solver'))

from verity_solver.shape import Shape
from verity_solver.player import Player
from verity_solver.game_state import GameState

if __name__ == '__main__':

    left = Player(Shape.SQUARE, Shape.TRIANGLE, Shape.TRIANGLE)
    middle = Player(Shape.CIRCLE, Shape.SQUARE, Shape.SQUARE)
    right = Player(Shape.TRIANGLE, Shape.CIRCLE, Shape.CIRCLE)

    verity = GameState(left, middle, right)

    instructions = GameState.solve(verity)

    for ins in instructions:
        print(ins)
