class Move:

    # Initializing class
    def __init__(self, value):
        self._value = value

    # Creating greed only property
    @property
    def value(self):
        return self._value

    # Method that checks if value is a valid entry
    def is_valid(self):
        return 1 <= self._value <= 9

    # Get row of entered value
    def get_row(self):
        if self._value in (1, 2, 3):
            return 0 # First row
        elif self._value in (4, 5, 6):
            return 1 # Second row
        else:
            return 2 # Third row

    # Get column of entered value    
    def get_column(self):
        if self._value in (1, 4, 7):
            return 0 # First column
        elif self._value in (2, 5, 8):
            return 1 # Second column
        else:
            return 2 # Third column
        

#        col0 col1 col2
# row 0: | 1 | 2 | 3 |
# row 1: | 4 | 5 | 6 |
# row 2: | 7 | 8 | 9 |
        