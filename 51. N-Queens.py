class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize an empty board
        board = [['.' for _ in range(n)] for _ in range(n)]
        # List to store all valid solutions
        solutions = []

        # Function to check if placing a queen at position (row, col) is valid
        def is_valid(board, row, col):
            # Check if there's any queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Check if there's any queen in the upper-left diagonal
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            # Check if there's any queen in the upper-right diagonal
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            return True

        # Backtracking function to place queens on the board
        def backtrack(row):
            if row == n:
                # Found a valid solution, add it to the list of solutions
                solutions.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    # Place queen at (row, col)
                    board[row][col] = 'Q'
                    # Move to the next row
                    backtrack(row + 1)
                    # Backtrack by removing the queen from (row, col)
                    board[row][col] = '.'

        # Start the backtracking process
        backtrack(0)
        return solutions
        
