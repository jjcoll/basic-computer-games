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


# get Bot move
def computerMove():
    a = 0
    while not (a in available):
        a = str(random.randint(1, 10))
    return a


# get User move
def userMove():
    while True:
        a = input('Where do you want to place a token: ')
        if a in available:
            return a
        else:
            print('That is not a valid box, enter number from', ' '.join(a))


def checkWinner(r1, r2, r3):
    for r in (r1, r2, r3):
        if len(set(r)) == 1:
            return True
    for i in range(0, 3):
        if len({r1[i], r2[i], r3[i]}) == 1:
            return True
    if len({r1[0], r2[1], r3[2]}) == 1:
        return True
    if len({r1[2], r2[1], r3[0]}) == 1:
        printBoard()
        return True


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
