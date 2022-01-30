import math
import random
import time

def printBoard(board):
  n = len(board)
  f = open("results/simulatedAnnealing/"+str(numberOfQueens)+'-queens.txt', "a")
  f.write("--------------------------------\n\n")
  for i in range(n-1, -1, -1):
    for j in range(n):
      if board[j] == i: 
        f.write(' Q ')
      else: 
        f.write(' - ')
    f.write("\n")

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

def move(n, board, h, temperature):
  boardTemperature = list(board)
  found = False
 
  while not found:
    boardTemperature = list(board)

    # seleciona um movimento aleatório
    new_row = random.randint(0,n-1)
    new_col = random.randint(0,n-1)
    boardTemperature[new_col] = new_row
    new_h = calculateObjectiveFunction(n, boardTemperature)

    # se o movimento for otimo, aceita
    if new_h < h:
      found = True
    else:
      # senão calcula o risco
      # se for arriscado rejeita(continua o laço), senão aceita
      delta_e = h - new_h
      accept_prob = min(1,math.exp(delta_e/temperature))
      found = random.random() <= accept_prob
   
  return boardTemperature


def simulatedAnnealing(n, board):
  temperature = n**2
  cooling_rate = 0.95
  h = calculateObjectiveFunction(n, board)
  steps = 0
   
  while h > 0:
    board = move(n, board,h, temperature)
    h = calculateObjectiveFunction(n, board)

    # diminui aceitavelmente a temperatura
    n_temp = max(temperature * cooling_rate,0.01)
    temperature = n_temp

    steps += 1
    if steps >= 1000:
      break

  if h==0:
    return steps, board

  return steps, board



if __name__ == "__main__":

  queens = [5, 7, 8, 9, 10]

  for queen in range(len(queens)):
    
    mean_time = 0
    queenProblem = 0
    
    for ex in range(10):
      numberOfQueens = queens[queen]

      start = time.time()

      board = generateBoard(numberOfQueens)

      print("\nFinal = ")
      steps, board = simulatedAnnealing(numberOfQueens, board)
      
      printBoard(board)
      h = calculateObjectiveFunction(numberOfQueens, board)

      end = time.time()
      total = end-start
      mean_time += total
      f = open("results/simulatedAnnealing/"+str(numberOfQueens)+'-queens.txt', "a")
      f.write(f"h(final): {h}\n")
      f.write(f"número de passos: {steps}\n")

      if h != 0:
        f.write("Limite de movimentos atingido\n")
      else:
        f.write("Estado objetivo alcançado\n")
      f.write(f"\nTempo total: {total*1000} ms\n\n")
      f.close()

    f = open("results/simulatedAnnealing/"+str(numberOfQueens)+'-queens.txt', "a")
    f.write(f"\nMédia de tempo: {(mean_time/10)*1000} ms")
    f.close()