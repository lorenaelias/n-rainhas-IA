import numpy as np
import copy
import time

class IterativeDFS:
  def __init__(self, n):
    self.n = n
    self.depth = 0
    self.queensPositions = dict()
    self.board = [[0 for i in range(n)] for j in range(n)]

  def printSolution(self):
    f = open("results/"+str(self.n)+'-queens.txt', "a")
    f.write(f'\n\nExecução {ex+1}--------------------------------\n\n')
    f.write("Profundidade: " + str(self.depth))
    f.write("\n")
    for i in range(self.n):
      for j in range(self.n):
        if (self.board[i][j] == 1):
          f.write("Q ")
        else:
          f.write("- ")
      f.write("\n")
    f.write("----------------------------------------------------\n")
    f.close()

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

  queens = [10]

  for queen in range(len(queens)):
    
    mean_time = 0
    queenProblem = 0
    
    for ex in range(10):
      numberOfQueens = queens[queen]

      start = time.time()

      queenProblem = IterativeDFS(n = numberOfQueens)

      # inserir rainhas no board
      for i in range(numberOfQueens):
        j = generateRandomNumber(0, numberOfQueens)
        queenProblem.board[i][j] = 1
        queenProblem.queensPositions[i] = j
      
      while queenProblem.solve() == False:
        queenProblem.depth += 1

      end = time.time()
      total = end-start
      mean_time += total
      f = open("results/"+str(numberOfQueens)+'-queens.txt', "a")
      f.write(f"\nTempo total: {total*1000} ms\n\n")
      f.close()

    f = open("results/"+str(numberOfQueens)+'-queens.txt', "a")
    f.write(f"\nMédia de tempo: {(mean_time/10)*1000} ms")
    f.close()