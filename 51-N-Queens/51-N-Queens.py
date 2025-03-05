class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                solution.append([''.join(row_state) for row_state in board])
                return
            for col in range(n):
                if column[col] + diagonal[row + col] + anti_diagonal[n - row + col] == 0:
                    board[row][col] = "Q"
                    column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 1
                    backtrack(row + 1)
                    column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 0
                    board[row][col] = "."
        solution = []
        board = [["."] * n for _ in range(n)]
        column = [0] * n
        diagonal = [0] * (2 * n)
        anti_diagonal = [0] * (2 * n)
        backtrack(0)
        return solution