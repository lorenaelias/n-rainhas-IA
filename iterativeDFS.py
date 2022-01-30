import numpy as np
import copy

class IterativeDFS:
  def __init__(self, n):
    self.n = n
    self.depth = 0
    self.queensPositions = dict()
    self.board = [[0 for i in range(n)] for j in range(n)]

  def printSolution(self):
    for i in range(self.n):
      for j in range(self.n):
        if (self.board[i][j] == 1):
          print("Q", end=" ")
        else:
          print("-", end=" ")
      print()
    print("---------------------------------")

  def isValidQueen(self, board, row, col):
    for i in range(self.n):
      if (self.board[row][i] == 1 and col != i):
        return False

    for i in range(self.n):
      if (self.board[i][col] == 1 and row != i):
        return False

    (i, j) = (row, col)
    while i >= 0 and j >= 0:
      if (self.board[i][j] == 1 and (i != row and j != col)):
        return False
      i -= 1
      j -= 1

    (i, j) = (row, col)
    while i >= 0 and j < self.n:
      if self.board[i][j] == 1 and (i != row and j != col):
        return False
      i -= 1
      j += 1

    (i, j) = (row, col)
    while i < self.n and j < self.n:
      if self.board[i][j] == 1 and (i != row and j != col):
        return False
      i += 1
      j += 1

    (i, j) = (row, col)
    while i < self.n and j <= 0:
      if self.board[i][j] == 1 and (i != row and j != col):
        return False
      i += 1
      j -= 1
    
    return True

  def isValidBoard(self, board):
    for row in range(self.n):
      for col in range(self.n):
        if (self.board[row][col] == 1):
          if (self.isValidQueen(self.board, row, col) == False):
            return False
    return True

  def solveAuxRecursion(self, board, row, currDepth):
    if self.isValidBoard(self.board):
      return True

    if (row >= self.n):
      return False

    if(currDepth >= self.depth):
      return False

    colQueenPosition = self.queensPositions[row]
    self.board[row][colQueenPosition] = 0

    for col in range(self.n):

      self.board[row][col] = 1

      if self.solveAuxRecursion(self.board, row + 1, currDepth + 1):
        return True

      self.board[row][col] = 0

    self.board[row][colQueenPosition] = 1

    return False

  def solve(self):
    currDepth = 0

    print("---------------------------------")
    print("Profundidade: " + str(self.depth))

    if (self.solveAuxRecursion(self.board, 0, currDepth) == False):
      print("\nSolução não encontrada!\n")
      return False

    print("\nFoi encontrada uma solução!\n")
    self.printSolution()
    return True

def generateRandomNumber(min, max):
  return np.random.randint(min, max)

if __name__ == '__main__':
  numberOfQueens = int(input('Número de rainhas: '))
  
  queenProblem = IterativeDFS(n = numberOfQueens)

  # inserir rainhas no board
  for i in range(numberOfQueens):
    j = generateRandomNumber(0, numberOfQueens)
    queenProblem.board[i][j] = 1
    queenProblem.queensPositions[i] = j
  
  while queenProblem.solve() == False:
    queenProblem.depth += 1