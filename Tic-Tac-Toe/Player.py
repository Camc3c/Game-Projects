import random
from Move import Move


class Player:

    # Initialize player and computer markers
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    # Initializing class
    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    # Creating read only property for human player
    @property
    def is_human(self):
        return self._is_human
    
    # Creating read only property for marker
    @property
    def marker(self):
        return self._marker
    
    # Method for getting moves
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else: 
            return self.get_computer_move()

    # Method for getting the players move    
    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move
    
    # Method for computers move
    def get_computer_move(slef):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print("Computer move (1-9):", move.value)
        return move
    