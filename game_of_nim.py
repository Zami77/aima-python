from typing import List, Tuple
from games import *

class GameOfNim(Game):
    def __init__(self, board=[0, 5, 3, 1]) -> None:
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=self.get_moves(board))
    
    def get_moves(self, game_board: List[int]) -> List[Tuple[int, int]]:
        moves = []
        for row in range(len(game_board)):
            for num_picked in range(1, game_board[row] + 1):
                moves.append((row, num_picked))
        
        return moves


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    # print(nim.result(nim.initial, (1,3) ))
    # utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    # if (utility < 0):
    #     print("MIN won the game")
    # else:
    #     print("MAX won the game")