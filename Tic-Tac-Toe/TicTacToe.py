from Player import Player
from Board import Board


class TicTacToeGame:

    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        # Ask the user if they would like to
        # play another round.    
        while True:
                
                # Get move, check tie, check game over
                while True:
                     
                     player_move = player.get_move()