def assignItem(detectplayer):
    if (myList[a] == a):
        myList[a]=detectplayer
    elif(myList[a]==detectplayer):
        print('You have made this choice before')
    else:
        print('The other player select this cell before')
def printGuzelceBastir():
    for i in range(n):
        for z in range(n):
            if ((z + (i * n)) < 10):
                print(myList[z + (i * n)], end="  ")
            else:
                print(myList[z + (i * n)], end=" ")
            if ((z + (i * n)) % n == n-1 ):
                print()

def checkHorizontal(detectplayer):
    count_number1=0
    k = list(range(n*n - 1))
    for b in k:
        if (myList[b] == myList[b + 1]):
            count_number1 += 1
        if ((b + 1) % n == 0):
            count_number1 = 0
        if (count_number1 == n-1 and myList[b]==detectplayer):
            return True



def checkVertical(detectplayer):
    for x in range(n):
        count_num = 0
        g = x
        for y in range(n - 1):
            if (myList[g] == myList[g + n]):
                g = g + n
                count_num += 1
        if (count_num == n-1 and myList[g]==detectplayer):
            return True

def checkDiagonally(detectplayer):
    diag=0
    count_diag=0
    for t in range(n-1):
        if (myList[diag]==myList[diag+n+1]):
            count_diag+=1
            diag=diag+n+1
            if (count_diag==n-1 and myList[diag]==detectplayer):
                return True
    reverseDiag=n-1
    count_reverseDiag=0
    for p in range(n-1):
        if (myList[reverseDiag]==myList[reverseDiag+n-1]):
            count_reverseDiag+=1
            reverseDiag=reverseDiag+n-1
            if (count_reverseDiag==n-1 and myList[reverseDiag]==detectplayer):
                return True


def checkIfGameOver(detectplayer):
    if ( checkVertical(detectplayer) or  checkHorizontal(detectplayer) or checkDiagonally(detectplayer)):
        return True
    else:
        return False


def checkInputtype(board):
    if ((board).isdigit() and int(board)>1):
        return True
    else:
        return False

def checkInputplayer1(celis):
    if ((celis).isdigit() and int(celis)>=0 and int(celis)<n*n):
        return True
    else:
        return False


def checkInputplayer2(celis2):
    if ((celis2).isdigit() and int(celis2)>=0 and int(celis2)<n*n):
        return True
    else:
        return False




board=input('What size of board?')
while True:
    if checkInputtype(board):
        break
    else:
        print('Please enter a valid number')
        board=input('What size of board?')
n = int(board)
myList = list(range(n * n))
printGuzelceBastir()
while True:
    celis = input('Player 1 turn-->')
    while True:
        if checkInputplayer1(celis):
            break
        else:
            print('Please enter a valid number')
            celis = input('Player 1 turn-->')
    a=int(celis)
    assignItem('X')
    printGuzelceBastir()
    checkHorizontal('X')
    checkVertical('X')
    checkDiagonally('X')
    if (checkIfGameOver('X')):
        print("Winner: X")
        break
    if (all(isinstance(item,str) for item in myList)):
        print('Game over:There is no winner')
        break
    while True:
        celis2 = input('Player 2 turn-->')
        if checkInputplayer2(celis2):
            break
        else:
            print('Please enter a valid number')
    a=int(celis2)
    assignItem('O')
    printGuzelceBastir()
    checkHorizontal('O')
    checkVertical('O')
    checkDiagonally('O')
    if (checkIfGameOver('O') ):
        print("Winner: O")
        break
    if (all(isinstance(item,str) for item in myList)):
        print('Game over:There is no winner')
        break 












