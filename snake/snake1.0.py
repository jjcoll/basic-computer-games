import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from random import randint
import time


def main(stdscr):
    curses.curs_set(0)  # remove cursor
    stdscr.nodelay(True)  # will not hang the program when getkey()

    snake = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6]]

    key = "KEY_RIGHT"


    # debugging
    # win = curses.newwin(1, 50, 0, 0)

    # Color pairs
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)



    # apple and score
    apple = [20, 20]
    score = 0

    # max x and y
    y, x = stdscr.getmaxyx()

    while True:
            
        time.sleep(0.1)
        try:
            new_key = stdscr.getkey()
            key = new_key
        except:
            new_key = None
        if key == "KEY_LEFT":
            snake.insert(0, [snake[0][0], snake[0][1] -1])
            snake.pop()
        elif key == "KEY_RIGHT":
            snake.insert(0, [snake[0][0], snake[0][1] +1])
            snake.pop()
        elif key == "KEY_UP":
            snake.insert(0, [snake[0][0] -1, snake[0][1]])
            snake.pop()
        elif key == "KEY_DOWN":
            snake.insert(0, [snake[0][0] +1, snake[0][1]])
            snake.pop()

        stdscr.clear()
        stdscr.addstr(apple[0], apple[1], "#")



        if snake[0] in snake[1:]:  # run over yourself
            # for i in snake:
            #     stdscr.addstr(i[0], i[1], "0")
            # stdscr.addstr(snake[0][0], snake[0][1], "0", RED_AND_BLACK)
            stdscr.addstr(0, 0, 'You ran over yourself')
            # stdscr.refresh()
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
            if key == "KEY_LEFT":
                snake.append([snake[0][0], snake[0][1] +1])
            elif key == "KEY_RIGHT":
                snake.append([snake[0][0], snake[0][1] -1])
            elif key == "KEY_UP":
                snake.append([snake[0][0] +1, snake[0][1]])
            elif key == "KEY_DOWN":
                snake.append([snake[0][0] -1, snake[0][1]])
            stdscr.refresh()

        for i in snake:
            stdscr.addstr(i[0], i[1], "0")
            # stdscr.addstr(0, 0, f'head:{snake[0]} b1:{snake[1]} b2:{snake[2]} b3:{snake[3]} b4:{snake[4]}')  
            stdscr.addstr(0, 0, f'Score: {score}')
        stdscr.refresh()
    
wrapper(main)
