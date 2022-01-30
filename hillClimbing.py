import random
import time

def printBoard(board):
  n = len(board)
  f = open("results/hillClimbing/"+str(n)+'-queens.txt', "a")
  for i in range(n-1, -1, -1):
    for j in range(n):
      if board[j] == i: 
        f.write(' Q ')
      else: 
        f.write(' - ')
    f.write("\n")
  f.close()

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


  # fica no laço até atingir o estado objetivo ou atingir o limite de iterações
  while(numMovements < 1000):
    # pega os proximos movimentos otimos possiveis
    flag, newHeuristicValue, col, row = nextMovement(heuristicValue, board)

    f = open("results/hillClimbing/"+str(numberOfQueens)+'-queens.txt', "a")
    if(flag == False):    # nao encontrou nenhum movimento otimo
      if not test:
        f.write("\n\nFinal: ")
        printBoard(board)
        print("h(final): ", heuristicValue)
        print("Número de movimentos: ", numMovements)
        f.write("Atingiu um máximo local")
      return numMovements, board, heuristicValue
    elif newHeuristicValue == 0:       # atingiu o estado objetivo
      board[col] = row
      if not test:
        f.write("\n\nFinal: ")
        printBoard(board)
        print("h(final): ", newHeuristicValue)
        print("Número de movimentos: ", numMovements)
        f.write("Atingiu o estado objetivo")
      return numMovements, board, heuristicValue
    else:               # encontrou um movimento otimo
      board[col] = row

    h = newHeuristicValue
    numMovements += 1
  
  if not test:
    f.write("\n\nFinal: ")
    printBoard(board)
    print(numMovements)
    f.write("Alcançou limite de movimentos e não encontrou solução")

  f.close()

  return numMovements, board, newHeuristicValue



if __name__ == "__main__":

  queens = [5, 7, 8, 9, 10]

  for queen in range(len(queens)):
    
    mean_time = 0
    queenProblem = 0
    
    for ex in range(10):
      numberOfQueens = queens[queen]

      start = time.time()

      board = generateBoard(numberOfQueens)
      numMovements, board, h = hillClimbing(numberOfQueens, board)

      end = time.time()
      total = end-start
      mean_time += total
      f = open("results/hillClimbing/"+str(numberOfQueens)+'-queens.txt', "a")
      f.write(f"\nTempo total: {total*1000} ms\n\n")
      f.close()

    f = open("results/hillClimbing/"+str(numberOfQueens)+'-queens.txt', "a")
    f.write(f"\nMédia de tempo: {(mean_time/10)*1000} ms")
    f.close()