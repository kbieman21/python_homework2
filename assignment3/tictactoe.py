# tictactoe.py
# Beginner-friendly Tic-Tac-Toe

class TicTacToeException(Exception):
    """Custom exception for invalid moves."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    # List of allowed move names (must match exactly what the user types)
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        # Create a 3x3 board filled with spaces
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "X"   # X always starts

    def __str__(self):
        """Return a printable version of the board."""
        b = self.board_array
        return (
            f" {b[0][0]} | {b[0][1]} | {b[0][2]} \n"
            f"-----------\n"
            f" {b[1][0]} | {b[1][1]} | {b[1][2]} \n"
            f"-----------\n"
            f" {b[2][0]} | {b[2][1]} | {b[2][2]} \n"
        )

    def move(self, move_string):
        """Place an X or O on the board if the move is valid."""
        # Check if the move name is allowed
        if move_string not in Board.valid_moves:
            raise TicTacToeException("That's not a valid move.")

        # Convert the move name into a row and column
        index = Board.valid_moves.index(move_string)
        row = index // 3
        col = index % 3

        # Check if the spot is already taken
        if self.board_array[row][col] != " ":
            raise TicTacToeException("That spot is taken.")

        # Place the current player's mark
        self.board_array[row][col] = self.turn

        # Switch turns
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def is_full(self):
        """Return True if every spot on the board is filled."""
        for row in self.board_array:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def check_winner(self):
        """Return 'X' or 'O' if someone has three in a row, otherwise None."""
        b = self.board_array

        # Check rows
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] != " ":
                return b[i][0]

        # Check columns
        for i in range(3):
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] != " ":
                return b[0][i]

        # Check diagonals
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] != " ":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] != " ":
            return b[0][2]

        return None

    def whats_next(self):
        """Decide what happens next in the game."""
        winner = self.check_winner()
        if winner:
            return (True, f"{winner} wins!")

        if self.is_full():
            return (True, "Cat's Game.")

        # Game is still going
        return (False, f"{self.turn}'s turn.")


# ====================== Main game loop ======================
if __name__ == "__main__":
    board = Board()
    print("Welcome to Tic-Tac-Toe!")
    print("Type a move such as: upper left, center, lower right")
    print()

    while True:
        # Show the board
        print(board)

        # Ask the board what should happen next
        game_over, message = board.whats_next()
        print(message)

        if game_over:
            break

        # Ask the player for a move
        try:
            user_input = input(f"{board.turn}'s move: ").strip().lower()
            board.move(user_input)
        except TicTacToeException as e:
            print("Error:", e.message)
            print("Try again.\n")

    print("Thanks for playing!")