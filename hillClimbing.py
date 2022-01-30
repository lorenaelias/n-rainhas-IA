import random
import time

def printBoard(board):
  n = len(board)
  for i in range(n-1, -1, -1):
    for j in range(n):
      if board[j] == i: 
        print(' Q ', end='')
      else: 
        print(' - ', end='')
    print()

def generateBoard(n):
  board = [random.randint(0, n-1) for _ in range(n)]
  return board

def calculateObjectiveFunction(n, board):
  h = 0
  for i in range(n):
    for j in range(i+1, n):

      if board[i] == board[j]:   # checagem de rainhas na mesma linha
        h += 1

      offset = j - i

      # checagem das diagonais
      if (board[j] == board[i]-offset) or (board[j] == board[i] + offset):
        h+=1

  return h

def nextMovement(h, board, flag=False):

  nextMovesHeuristic = {}
  n = len(board)

  for col in range(0, n):
    for row in range(n):
      if board[col] == row: continue # se a rainha estiver na mesma linha, nao faz nada

      auxBoard = board.copy()
      auxBoard[col] = row
      nextMovesHeuristic[(col, row)] = calculateObjectiveFunction(n, auxBoard)

  minHeuristicMove = []
  minHeuristicValue = h

  # encontrando o minimo valor de heuristica para todos os movimentos possiveis
  for value in nextMovesHeuristic.values():
    if value < minHeuristicValue:
      minHeuristicValue = value

  # cria uma lista com todos os movimentos com o valor minimo de heuristica
  for cordinates, value in nextMovesHeuristic.items():
    if value == minHeuristicValue:
      minHeuristicMove.append(cordinates)

  if flag and minHeuristicValue == h: 
    return False, h, -1, -1  # nao encontrou nenhum movimento otimo


  # seleciona um movimento aleatorio da lista de movimentos com o valor minimo de heuristica
  if len(minHeuristicMove) > 0:
    x = random.randint(0, len(minHeuristicMove)-1)
    return True, minHeuristicValue, minHeuristicMove[x][0], minHeuristicMove[x][1]
  else: 
    return False, minHeuristicValue, -1, -1



def hillClimbing(n, board, test = False):
  
  heuristicValue = calculateObjectiveFunction(n, board)
  
  if not test:
    print("h(inicial) =", heuristicValue)
  
  newHeuristicValue = 0
  numMovements = 0


  ## fica no laço até atingir o estado objetivo ou atingir o limite de iterações
  while(numMovements < 1000):
    ## get optimal next moves 
    flag, newHeuristicValue, col, row = nextMovement(heuristicValue, board)

    if(flag == False):    # nao encontrou nenhum movimento otimo
      if not test:
        print("\nFinal = ")
        printBoard(board)
        print("h(final) =", heuristicValue)
        print("Número de movimentos: ", numMovements)
        print("Atingiu um máximo local")
      return numMovements, board, heuristicValue
    elif newHeuristicValue == 0:       # atingiu o estado objetivo
      board[col] = row
      if not test:
        print("\nFinal = ")
        printBoard(board)
        print("h(final) =", newHeuristicValue)
        print("Número de movimentos: ", numMovements)
        print("Atingiu o estado objetivo")
      return numMovements, board, heuristicValue
    else:               # encontrou um movimento otimo
      board[col] = row

    h = newHeuristicValue
    numMovements += 1
  
  if not test:
    print("\nFinal = ")
    printBoard(board)
    print(numMovements)
    print("Alcançou limite de movimentos e não encontrou solução")

  return numMovements, board, newHeuristicValue



if __name__ == "__main__":

  start = time.time()

  numberOfQueens = 8
  board = generateBoard(numberOfQueens)

  print("Tabuleiro inicial")
  printBoard(board)

  numMovements, board, h = hillClimbing(numberOfQueens, board)

  end = time.time()

  print(f"Tempo total: {(end-start)*1000} ms")

  print()