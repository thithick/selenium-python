# https://leetcode.com/problems/valid-sudoku/
# Algorithm: How to check if a sudoku board is valid
# Check if the rows and columns contain values 1-9, without repetition.
# If any row or column violates this condition, the Sudoku board is invalid.
# Check to see if each of the 9 sub-squares contains values 1-9, without repetition.
# If they do, the Sudoku board is valid; otherwise, it is invalid.
'''Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true '''

import sys

def validSudoku(lst):
    n1=len(lst)
    for i in lst:
        list = str(i).split(",")
        # list = str(i).split(",")
        print(list)

if __name__=='__main__':
    lst = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    validSudoku(lst)
