# This works with one player, the computer chooses randomly by generating a random integer
import random

r1 = ['1', '2', '3']
r2 = ['4', '5', '6']
r3 = ['7', '8', '9']

def printBoard():
    print(' '.join(r1))
    print(' '.join(r2))
    print(' '.join(r3))

def replaceBox(availableBoxes, boxToReplace):
        if boxToReplace in availableBoxes:
            if boxToReplace in r1:
                r1[r1.index(boxToReplace)] = coin[turn % 2]
            elif boxToReplace in r2:
                r2[r2.index(boxToReplace)] = coin[turn % 2]
            elif boxToReplace in r3:
                r3[r3.index(boxToReplace)] = coin[turn % 2]
            availableBoxes.pop(availableBoxes.index(boxToReplace))

def simulateReplaceBox(availableBoxes, boxToReplace, r1, r2, r3, coin):
    if boxToReplace in availableBoxes:
        if boxToReplace in r1:
            r1[r1.index(boxToReplace)] = coin
        elif boxToReplace in r2:
            r2[r2.index(boxToReplace)] = coin
        elif boxToReplace in r3:
            r3[r3.index(boxToReplace)] = coin

# get Bot move
def computerMove():
    copyAvailable = available.copy()
    for i in copyAvailable:
        r1Copy = r1.copy()
        r2Copy = r2.copy()
        r3Copy = r3.copy()
        simulateReplaceBox(copyAvailable, i, r1Copy, r1Copy, r3Copy, 'X')
        if checkWinner(r1Copy, r2Copy, r3Copy):
            print('I found a way to win -------------')
            return i
        else:
            print('no way to win --------------------')
            continue
    for i in copyAvailable:
        r1Copy = r1.copy()
        r2Copy = r2.copy()
        r3Copy = r3.copy()
        simulateReplaceBox(copyAvailable, i, r1Copy, r1Copy, r3Copy, '0')
        if checkWinner(r1Copy, r2Copy, r3Copy):
            print('I found a way not to loose -------------')
            return i
        else:
            print('no way not to loose --------------------')
            continue
    a = 0
    while not (a in available):
        a = str(random.randint(1, 10))
    return a


def computerMove2():
    # empate
    if available == 0:
        return 0
    # win
    if checkWinner(r1, r2, r3) == 1 and coin[turn % 2] == 'X':
        return 1
    else:
        return -1


# get User move
def userMove():
    while True:
        a = input('Where do you want to place a token: ')
        if a in available:
            return a
        else:
            print('That is not a valid box, enter number from', ' '.join(a))


# evaluar si el tablero se puede jugar
def checkWinner(r1, r2, r3):
    for r in (r1, r2, r3):
        if len(set(r)) == 1:
            return 1
    for i in range(0, 3):
        if len(set([r1[i], r2[i], r3[i]])) == 1:
            return 1
    if len(set([r1[0], r2[1], r3[2]])) == 1 or len(set([r1[2], r2[1], r3[0]])) == 1:
        return 1
    


play = 0
turn = 0
coin = ('0', 'X')
available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# run game
while play < 9:
    print('\n\n\n\n\n')
    printBoard()
    print('It is the turn of', coin[turn % 2])
    if coin[turn % 2] == 'X':
        replaceBox(available, computerMove())
    else:
        replaceBox(available, userMove())
    if checkWinner(r1, r2, r3):
        printBoard()
        print(coin[turn % 2], 'has won')
        exit()
    turn += 1
    play += 1
print('No one won better luck next time!')
