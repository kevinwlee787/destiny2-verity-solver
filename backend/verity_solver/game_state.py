from player import Player
from typing import List

class GameState:
    def __init__(self, p1: Player, p2: Player, p3: Player):
        self.player1 = p1
        self.player2 = p2
        self.player3 = p3
    
    @staticmethod
    def solve(gs: 'GameState') -> List[str]:
        ret = []

        while not gs.player1.is_complete():
            duplicate_shape = gs.player1.duplicate_shape()

            if not gs.player2.contains(duplicate_shape):
                other_duplicate_shape = gs.player2.duplicate_shape()
                gs.player1.swap(duplicate_shape, other_duplicate_shape)
                gs.player2.swap(other_duplicate_shape, duplicate_shape)
                ret.append(('Left', duplicate_shape, 'Mid', other_duplicate_shape))

            elif not gs.player3.contains(duplicate_shape):
                other_duplicate_shape = gs.player3.duplicate_shape()
                gs.player1.swap(duplicate_shape, other_duplicate_shape)
                gs.player3.swap(other_duplicate_shape, duplicate_shape)
                ret.append(('Left', duplicate_shape, 'Right', other_duplicate_shape))

        while not gs.player2.is_complete():
            duplicate_shape = gs.player2.duplicate_shape()

            if not gs.player3.contains(duplicate_shape):
                other_duplicate_shape = gs.player3.duplicate_shape()
                gs.player2.swap(duplicate_shape, other_duplicate_shape)
                gs.player3.swap(other_duplicate_shape, duplicate_shape)
                ret.append(('Mid', duplicate_shape, 'Right', other_duplicate_shape))
            
        return ret
        