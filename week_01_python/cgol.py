def createNewBoard(rows, cols):
  board = []
  for i in range(rows):
      col = []
      for j in range(cols):
          col.append('.')
      board.append(col)
  return board

def printBoard(board):
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            print(board[i][j] + " ", end = "")
        print("\n")

def setCell(board, r, c, val):
    board[r][c] = val

def copyBoard(oldBoard):
    rows = len(oldBoard)
    cols = len(oldBoard[0])
    newBoard = createNewBoard(len(oldBoard), len(oldBoard[0]))
    for i in range(rows):
        for j in range(cols):
            newBoard[i][j] = oldBoard[i][j]
    return newBoard

def isGameOver(board):
    numAlive = 0
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            if isAlive(board, i, j):
                return False
    return True

def getNextGenCell(board, r, c):
    numNeighbors = countNeighbors(board, r, c)
    if isAlive(board,r,c):
        if numNeighbors == 3 or numNeighbors == 2:
            return 'L'
        else:
            return '.'
    else:
        if numNeighbors == 3:
            return 'L'
        else:
            return '.'


def isAlive(board, r, c):
    if (r > len(board) - 1) or c > len(board[0]) -1 or r < 0 or c < 0:
        return False
    else:
        if board[r][c] == 'L':
            return True
        else:
            return False

def generateNextBoard(board):
    rows = len(board)
    cols = len(board[0])
    newBoard = copyBoard(board)
    for i in range(rows):
        for j in range(cols):
            nextGenCellChar = getNextGenCell(board, i, j)
            setCell(newBoard, i, j, nextGenCellChar)
    return newBoard

def countNeighbors(board, r, c):
    livingNeighbors = 0

    if isAlive(board,r-1,c-1):
        livingNeighbors+=1

    if isAlive(board,r-1,c):
        livingNeighbors+=1

    if isAlive(board,r-1,c+1):
        livingNeighbors+=1

    if isAlive(board,r,c-1):
        livingNeighbors+=1

    if isAlive(board,r,c+1):
        livingNeighbors+=1

    if isAlive(board,r+1,c-1):
        livingNeighbors+=1

    if isAlive(board,r+1,c):
        livingNeighbors+=1

    if isAlive(board,r+1,c+1):
        livingNeighbors+=1

    return livingNeighbors

#call functions
size = int(input("What size would you like to make your board?"))
b = createNewBoard(size,size)
printBoard(b)

numLivingCells = int(input("How many living cells do you want?"))

for i in range(numLivingCells):
    print("Where would you like to place this cell?")
    r = int(input("row: "))
    c = int(input("col: "))
    setCell(b, r, c, 'L')

rounds = int(input("How many rounds would you like to play?"))

i = 0

while i < rounds:
    b = generateNextBoard(b)
    print("Generation: "+ str(i))
    printBoard(b)
    if isGameOver(b):
        print("Your populations all died. GAME OVER")
        break
    i+=1
