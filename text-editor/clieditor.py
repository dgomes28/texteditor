import curses
from curses import wrapper
import random

def main(stdscr):
    stdscr.clear()
    
    while KeyboardInterrupt:
        stdscr.keypad(True)
        i = random.randint(1, 100)/100
        j = random.randint(1, 100)/100
        stdscr.addstr(int(curses.LINES*i), int(curses.COLS/2*j) ,"Hello World")
        stdscr.getkey()
        stdscr.clear()
    

    stdscr.refresh()
    stdscr.getch()
    

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