import numpy as np 

class HillClimbing:
  def __init__(self, n):
    self.n = n
    self.board = [[0 for i in range(n)] for j in range(n)]
    self.state = [0 for i in range(n)]

  def printSolution(self):
    for i in range(self.n):
      for j in range(self.n):
        if (self.board[i][j] == 1):
          print("Q", end=" ")
        else:
          print("-", end=" ")
      print()
    print("---------------------------------")

  def fill(self, board, state):
    for i in range(self.n):
      for j in range(self.n):
        board[i][j] = state
  
  def generateBoard(self, board, state):
    fill(board, 0)
    for i in range(self.n):
      board[state[i]][i] = 1
  
  def getNeighbor(self, board, state):
    auxBoard = [[0 for i in range(self.n)] for j in range(self.n)]
    auxState = [0 for i in range(self.n)]

    auxState = state
    generateBoard(auxBoard, auxState)

    objectiveValue = calculateObjectiveFunction(auxBoard, auxState)

    neighborBoard = [[0 for i in range(self.n)] for j in range(self.n)]
    neighborState = [0 for i in range(self.n)]

    neighborState = state
    generateBoard(neighborBoard, neighborState)

    for i in range(self.n):
      for j in range(self.n):

        if (j != state[i]):
          neighborState[i] = j
          neighborBoard[neighborState[i]][i] = 1
          neighborBoard[state[i]][i] = 0

          auxObjective = calculateObjectiveFunction(neighborBoard, neighborState)
          if (auxObjective <= objectiveValue):
            objectiveValue = auxObjective
            auxState = neighborState
            generateBoard(auxBoard, auxState)

          neighborBoard[neighborState[i]][i] = 0
          neighborState[i] = state[i]
          neighborBoard[state[i]][i] = 1
    state = auxState
    fill(board, state)


  def solve(self):
    neighborBoard = [[0 for i in range(self.n)] for j in range(self.n)]
    neighborState = [0 for i in range(self.n)]

    neighborState = self.state
    self.generateBoard(neighborBoard, neighborState)

    while True:
      self.state = neighborState
      self.generateBoard(self.board, self.state)

      self.getNeighbor(neighborBoard, neighborState)

      if (neighborState == self.state):
        self.printSolution()
        break
      elif self.calculateObjectiveFunction(self.board, self.state) == calculateObjectiveFunction(neighborBoard, neighborState):
        neighborState[generateRandomNumber(0, self.n)] = generateRandomNumber(0, self.n)
        self.generateBoard(neighborBoard, neighborState)


def generateRandomNumber(min, max):
  return np.random.randint(min, max)

if __name__ == '__main__':
  numberOfQueens = int(input('Número de rainhas: '))
  
  queenProblem = HillClimbing(n = numberOfQueens)

  # inserir rainhas no board
  for i in range(numberOfQueens):
    queenProblem.state[i] = generateRandomNumber(0, numberOfQueens)
    queenProblem.board[state[i]][i] = 1

  queenProblem.solve()