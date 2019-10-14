import numpy as np

def isValidSudoku(board):
    blockCheck = []
    print(board[:1])
##    for i in range(len(board)):
##        for j in range(len(board[i])):
##            print("board[i][0:8] : " + str(board[i][0:9]) + " i: " + str(i))
##            print("board[0:8][j] : " + str(board[0:8][j]) + " j: " + str(j))
##            if board[i][j] is not ".":
##                if board[i][j] == board[i][0:8] or board [0:8][j]:
##                    continue
            
    

myList = [
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
isValidSudoku(myList)
