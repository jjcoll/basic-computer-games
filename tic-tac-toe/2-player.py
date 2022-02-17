r1 = ['1', '2', '3']
r2 = ['4', '5', '6']
r3 = ['7', '8', '9']

def winner(r1, r2, r3, p):
    # look at making this with for loop
    if len(set(r1)) == 1:
        return True
    if len(set(r2)) == 1:
        return True    
    if len(set(r3)) == 1:
        return True
    # vertical 3 in a row
    for i in range(0, 3):
        if len(set([r1[i], r2[i], r3[i]])) == 1:
            return True
    # diagonal
    if len(set([r1[0], r2[1], r3[2]])) == 1:
        return True
    if len(set([r1[2], r2[1], r3[0]])) == 1:
        printBoard()
        return True

# pritn state board
def printBoard():
    print(' '.join(r1))
    print(' '.join(r2))
    print(' '.join(r3))

# update board
def replaceBox(a):
    while True:
        n = input('Where do you want to place a token: ')
        if n in a:
            if n in r1:
                r1[r1.index(n)] = coin[turn % 2]
                a.pop(a.index(n))
                break
            elif  n in r2:
                r2[r2.index(n)] = coin[turn % 2]
                a.pop(a.index(n))
                break
            elif  n in r3:
                r3[r3.index(n)] = coin[turn % 2]
                a.pop(a.index(n))
                break
        else:
            print('That is not a valid box, enter number from', ' '.join(a))
        
# get number players
# num_players = 0
# while num_players != '2' and num_players != '1':
#     num_players = input('Select the number of players (1 or 2): ')

# game variables
play = 0
turn = 0
coin = ('0', 'X')
available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# run game
while play < 9:
    print('\n\n\n\n\n')
    printBoard()
    print('It is the turn of', coin[turn % 2])
    replaceBox(available)
    if winner(r1, r2, r3, coin[turn % 2]):
        printBoard()
        print(coin[turn % 2], 'has won')
        exit()
    turn += 1
    play += 1
print('No one won better luck next time!')
