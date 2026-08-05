from typing import List

"""
LeetCode 36: Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Approach:
Hash Set Validation across three passes:
1. Row Check: Iterate through each of the 9 rows and ensure no digit 1-9 repeats using a hash set.
2. Column Check: Iterate through each of the 9 columns using a hash set per column.
3. Sub-box Check: Map the 9 sub-boxes using formula `row = (square // 3) * 3 + i` and 
   `col = (square % 3) * 3 + j`, validating each 3x3 region with a separate hash set.

Complexity Analysis:
- Time Complexity: O(1) since the Sudoku board size is fixed at 81 (9 x 9) cells.
- Space Complexity: O(1) auxiliary space as each set stores at most 9 numbers.
"""


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Validate rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        # 2. Validate columns
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        # 3. Validate 3x3 sub-boxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Valid Sudoku Board
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(valid_board) == True, "Test Case 1 Failed"

    # Test Case 2: Invalid Sudoku Board (Two 8s in the top-left 3x3 box)
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert (
        solution.isValidSudoku(invalid_board) == False
    ), "Test Case 2 Failed"

    print("All tests passed successfully!")