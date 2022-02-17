from random import randint

# Hangman Game
'''
Choose a random word from list
User enters letter guess
Check if guess is in the word
Loop until user guesses the word or runs out of lifes
'''

# Choosing the Game Mode
print('''Welcome to hangman, there are three game modes available
1.Animals
2.Sport
3.Countries''')
mode = int(input('Please enter the category you want to play (1, 2, 3): '))


# Getting file name
word = ''
if mode == 1:
    mode = 'animals.txt'
elif mode == 2:
    mode = 'sports.txt'
elif mode == 3:
    mode = 'countries.txt'
else:
    print('Please enter a valid option!')
    exit()

# word = 'eliot'

# Get random line
with open(mode, 'r') as f:
    line_count = 0
    for l in f:
        if l != '\n':
            line_count += 1
    line = randint(0, line_count)
    lines = f.readlines()

# Get random word
with open(mode, 'r') as f:
    lines = f.readlines()
    word = lines[line]
    word = word.lower()

# word = 'magellanic penguin'

# Game logic
valid_guess = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
user_guess = []
hidden_word = []
word_array = []
lives = 6

# range(len(word) - 1)
for i in  word:
    if i == ' ':
        hidden_word.append(' ')
    else:
        hidden_word.append('-')

print('hidden word', ''.join(hidden_word))
print(len(word))
print(len(hidden_word))

print(word)
for i in word:
    word_array.append(i)

# Variables
# print(word)
# print(''.join(hidden_word))

#Check if user has won
def have_won(i, j):
    if ''.join(i) == j:
        print('You have won')
        exit()

# Check if the guess is valid
def is_guess_valid(l):
    if len(l) == 1 and l in valid_guess:
        return True
    else:
        print('Please enter one letter')
        return False

# Check if letter is in secret word
def round(l, lives):
    if l in word:
        print('The letter is in the word')
        list(hidden_word)
        hidden_word[word_array.index(guess)] = guess
        print('Guess is correct')
        return lives
    else:
        lives -= 1
        return lives


def info():
    print('lives: ', lives)
    print('word: ', ''.join(hidden_word))

while lives > 0:
    have_won(hidden_word, word)
    info()
    guess = input('Please guess a letter: ')
    if is_guess_valid(guess):
        lives = round(guess, lives)

print('You ran  out of lives')

        

# Update the hidden_word
        # print('The letter is in the word')
        # list(hidden_word)
        # hidden_word[word_array.index(guess)] = guess
        # print(''.join(hidden_word))
        # print(word_array, user_guess)


# while lives > 0:
#     guess = input('Please guess a letter: ')
#     if ''.join(hidden_word) == word:
#         print('You have won')
#     elif len(guess) == 1 and guess in valid_guess:
#         if guess in user_guess:
#             print('You have already entered that letter')
#         else:
#             if guess in word:
#                 print('The letter is in the word')
#                 list(hidden_word)
#                 hidden_word[word_array.index(guess)] = guess
#                 print(''.join(hidden_word))
#                 print(word_array, user_guess)
#             else:
#                 print('The letter is not in the word')
#                 user_guess.append(guess)
#                 lives -= 1
#     else:
#         print('Please enter only one letter from the alphabet')


