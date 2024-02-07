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
                    # Getting player move and adding it to the board.
                    player_move = player.get_move()
                    board.submit_move(player, player_move)
                    board.print_board()
                    
                    # Game tie
                    if board.check_is_tie():
                        print("It's a tie! Try again.")
                        break
                    # Game over. PLayer wins
                    elif board.check_is_game_over():
                        print("Awesome! You won the game!")
                        break
                    else:
                        # Else. Get computer move and add it to the board.
                        computer_move = computer.get_move()
                        board.submit_move(computer, computer_move)
                        board.print_board()

                        # Game over. The computer wins
                        if board.check_is_game_over(computer, computer_move):
                            print("Oops... The computer won. Try again.")
                            break

                # Play again prompt 
                play_again = input("Would you like to play again? Enter X for YES or O for NO").upper()

                if play_again == "O":
                    print("Bye! Come back later!")
                    break
                elif play_again == "X":
                    self.start_new_round(board)
                else:
                    print("Your input was not valid but I will assume that you want play again.")
                    self.start_new_round(board)