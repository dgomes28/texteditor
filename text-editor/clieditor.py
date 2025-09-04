import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import random

# class clieditor:
#     def __init__(self)


def main(stdscr):
    stdscr.clear()
    editwin = curses.newwin(5,30, 2,1)
    # rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    
    box = Textbox(editwin)

    box.edit()

    message = box.gather()

    stdscr.refresh()



    # stdscr.refresh()
    
    while KeyboardInterrupt:
        curses.echo()            # Enable echoing of characters

        stdscr.keypad(True)

        i = random.randint(1, 100)/100
        j = random.randint(1, 100)/100
        stdscr.addstr(int(curses.LINES*i), int(curses.COLS/2*j) ,message)
        stdscr.getkey()
        stdscr.clear()
    

    # stdscr.refresh()
    # stdscr.getch()
    print(message)
    

wrapper(main)

# from curses import wrapper

# def main(stdscr):
#     # Clear screen
#     stdscr.clear()

#     # This raises ZeroDivisionError when i == 10.
#     for i in range(1, 11):
#         v = i-10
#         if v == 0:
#             stdscr.clear()
#             stdscr.addstr("Terminating")
#             stdscr.refresh()
#             stdscr.getch()
#         else:
#             stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
#             stdscr.getkey()
        
        


# wrapper(main)