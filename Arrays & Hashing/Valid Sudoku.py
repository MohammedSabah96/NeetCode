# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from collections import defaultdict


def is_valid_sudoku(board_list: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    square = defaultdict(set)  # (r // 3, c // 3)

    for r in range(9):
        for c in range(9):
            cell = board_list[r][c]
            if cell == ".":
                continue
            if (cell in rows[r]) or \
                    (cell in cols[c]) or \
                    (cell in square[(r // 3, c // 3)]):
                return False

            rows[r].add(cell)
            cols[c].add(cell)
            square[(r // 3, c // 3)].add(cell)

    return True


class Solution:
    def is_valid_sudoku(self, board_list: list[list[str]]) -> bool:
        return self.is_row_valid(board_list) and \
               self.is_col_valid(board_list) and \
               self.is_square_valid(board_list)

    def is_row_valid(self, board_list: list[list[str]]) -> bool:
        for row in board_list:
            if not self.is_valid_units(row):
                return False
        return True

    def is_col_valid(self, board_list: list[list[str]]) -> bool:
        for col in zip(*board_list):
            if not self.is_valid_units(col):
                return False
        return True

    def is_square_valid(self, board_list: list[list[str]]) -> bool:
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board_list[x][y]
                          for x in range(i, i + 3)
                          for y in range(j, j + 3)]

                if not self.is_valid_units(square):
                    return False
        return True

    @staticmethod
    def is_valid_units(units: list[str] or tuple[str]) -> bool:
        units = [i for i in units if i != "."]
        return len(set(units)) == len(units)


sol = Solution()

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(sol.is_valid_sudoku(board))
print(is_valid_sudoku(board))

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(sol.is_valid_sudoku(board))
print(is_valid_sudoku(board))
