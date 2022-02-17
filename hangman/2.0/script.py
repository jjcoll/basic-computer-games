from random import randint

# Choosing the Game Mode
print('''Welcome to hangman, there are three game modes available
1.Animals
2.Sport
3.Countries''')

# Getting file name
correct_mode = False
while correct_mode == False:
    mode = int(input('Please enter the category you want to play (1, 2, 3): '))
    word = ''
    if mode == 1:
        mode = 'animals.txt'
        correct_mode = True
    elif mode == 2:
        mode = 'sports.txt'
        correct_mode = True
    elif mode == 3:
        mode = 'countries.txt'
        correct_mode = True
    else:
        print('Please enter a valid option!')
        exit()

with open(mode, 'r') as f:
    line_count = 0
    for l in f:
        if l != '\n':
            line_count += 1
    line = randint(0, line_count)
    lines = f.readlines()

# Get random word
sec_word_array = []
with open(mode, 'r') as f:
    lines = f.readlines()
    sec_word = lines[line]
    for i in sec_word:
        if i != '\n':
            sec_word_array.append(i.lower())
sec_word = ''.join(sec_word_array)

# Hidden word
hidden_word_array = []
for i in sec_word:
    if i == ' ':
        hidden_word_array.append(' ')
    else:
        hidden_word_array.append('-')
hidden_word = ''.join(hidden_word_array)
# Game Logic
lives = 6
valid_guess = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
taken_guesses = []
while lives > 0:
    # print('The secret word is: ', sec_word)
    if hidden_word_array != sec_word_array:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour progress:', ''.join(hidden_word_array))
        print('The mode is:', mode)
        print('You have tried:', ' '.join(sorted(taken_guesses)))
        print('lives:', lives)
        guess = input('Please guess a letter: ')
        if guess in valid_guess:
            if guess in taken_guesses:
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have already tried', guess, 'please try another letter')
                input('Press any key to continue')
                continue
            else:
                if guess in sec_word_array:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCorrect!')
                    input('Press any key to continue')
                    taken_guesses.append(guess)
                    occurences = sec_word_array.count(guess)
                    # print('The letter', guess,'is', occurences,'times')
                    if occurences == 1:
                        index = sec_word_array.index(guess)
                        hidden_word_array[index] = guess
                    else:
                        indices = [i for i, x in enumerate(sec_word_array) if x == guess]
                        for i in indices:
                            hidden_word_array[i] = guess               
                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIncorrect')
                    lives -= 1
                    taken_guesses.append(guess)
                    print('You have', lives, 'lives left')
                    input('Press a key to continue')
                    continue
        else:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', guess, 'is not a valid input')
            print('Please enter only one letter\n\n\n\n\n')
            input('Press a key to contine')
            continue
    else:
        print('Congratulations You have won, the word was', sec_word)
        exit()
print('You ran out of lives, better luck next time, the word was', sec_word)
