import curses
from curses import wrapper
from random import randint
import time

# Initial Game Setup
def start_game(lenght=4, max_y=20, max_x=20):
    # direction = ("KEY_LEFT", "KEY_RIGHT", "KEY_UP", "KEY_DOWN")

    # Position of snake and direction
    snake = [[randint(lenght,max_y-1), randint(lenght,max_x-1)]]
    if snake[0][0] > (max_y // 2):
        direction = "KEY_UP"
    if snake[0][1] > (max_x // 2):
        direction = "KEY_LEFT"
    if snake[0][0] < (max_y // 2):
        direction = "KEY_DOWN"
    if snake[0][1] < (max_x // 2):
        direction = "KEY_RIGHT"
    for i in range(lenght):
        snake = grow_snake(direction, snake)

    # Poition of Apple
    apple = [randint(1, max_y-1), randint(1, max_x-1)]

    return (snake, direction, apple, 0)


# Update Position of Snake
def update_snake(move, arr):
    if move == "KEY_LEFT":
        arr.insert(0, [arr[0][0], arr[0][1] -1])
        arr.pop()
    elif move == "KEY_RIGHT":
        arr.insert(0, [arr[0][0], arr[0][1] +1])
        arr.pop()
    elif move == "KEY_UP":
        arr.insert(0, [arr[0][0] -1, arr[0][1]])
        arr.pop()
    elif move == "KEY_DOWN":
        arr.insert(0, [arr[0][0] +1, arr[0][1]])
        arr.pop()
    return arr

# Make Snake Grow
def grow_snake(move, arr):
    if move == "KEY_LEFT":
        arr.append([arr[0][0], arr[0][1] +1])
    elif move == "KEY_RIGHT":
        arr.append([arr[0][0], arr[0][1] -1])
    elif move == "KEY_UP":
        arr.append([arr[0][0] +1, arr[0][1]])
    elif move == "KEY_DOWN":
        arr.append([arr[0][0] -1, arr[0][1]])
    return arr
    

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True) 
    y, x = stdscr.getmaxyx()
    
    # Color Pairs
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)

    
    # Variable to start the game
    snake, key, apple, score = start_game(6, y, x)
    pace = 0.2


    while True:
        time.sleep(pace)
        try:
            new_key = stdscr.getkey()
            key = new_key
        except:
            new_key = None
        update_snake(key, snake)
        
        stdscr.clear()
        stdscr.addstr(apple[0], apple[1], "#")

        if snake[0] in snake[1:]:  # run over yourself
            stdscr.addstr(0, 0, 'You ran over yourself')
            stdscr.refresh()
            time.sleep(3)
            break

        if snake[0][0] == 0 or snake[0][0] == y or snake[0][1] == 1 or snake[0][1] == x:
            stdscr.addstr(0, 0, 'You hit a wall')
            stdscr.refresh()
            time.sleep(3)
            break
        
        if snake[0] == apple:
            score += 1
            apple = [randint(1,y-1), randint(1,x-1)]
            stdscr.addstr(apple[0], apple[1], "#")
            grow_snake(key, snake)
            if pace > 0.05: pace -= 0.01
            stdscr.refresh()

        for i in snake:
            stdscr.addstr(i[0], i[1], "0")
            stdscr.addstr(0, 0, f'Score: {score} Speed: {1/pace} ')
        stdscr.refresh()
    
wrapper(main)
