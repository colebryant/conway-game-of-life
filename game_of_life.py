import copy
from typing import List


class Solution:
    # function for running 1 generation
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_number = len(board)
        column_number = len(board[0])

        board_copy = copy.deepcopy(board)

        for r in range(row_number):
            for c in range(column_number):

                adjacent_cell = 0

                # check above row
                if r - 1 in range(row_number):
                    if c - 1 in range(column_number):
                        if board_copy[r - 1][c - 1] == 1:
                            adjacent_cell += 1
                    if board_copy[r - 1][c] == 1:
                        adjacent_cell += 1
                    if c + 1 in range(column_number):
                        if board_copy[r - 1][c + 1] == 1:
                            adjacent_cell += 1

                # check current row
                if c - 1 in range(column_number):
                    if board_copy[r][c - 1] == 1:
                        adjacent_cell += 1
                if c + 1 in range(column_number):
                    if board_copy[r][c + 1] == 1:
                        adjacent_cell += 1

                # check below row
                if r + 1 in range(row_number):
                    if c - 1 in range(column_number):
                        if board_copy[r + 1][c - 1] == 1:
                            adjacent_cell += 1
                    if board_copy[r + 1][c] == 1:
                        adjacent_cell += 1
                    if c + 1 in range(column_number):
                        if board_copy[r + 1][c + 1] == 1:
                            adjacent_cell += 1

                # determine survivability
                if adjacent_cell < 2:
                    board[r][c] = 0
                elif board[r][c] == 1 and 2 <= adjacent_cell <= 3:
                    board[r][c] = 1
                elif board[r][c] == 0 and adjacent_cell == 3:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

    # master function for looping multiple generations over board
    def generation(self, board: List[List[int]], number_generations: int) -> None:
        for n in range(number_generations):
            self.gameOfLife(board)
        return board


solution = Solution()

# board: list of lists, number of generations: integer
print(solution.generation([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], 1))
