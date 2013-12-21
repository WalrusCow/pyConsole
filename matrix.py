''' Cover the screen in green ones and zeroes, as if in the Matrix. '''
import time, sys
import random
from console import getTerminalSize

ESC = '\033'

def getLine(cols):
    ''' Create a matrix line. '''
    CHOICES = '000111 '
    line = ''.join(random.choice(CHOICES) for _ in range(cols))
    return line

def matrix():
    ''' Run the matrix. '''
    t = 0.05

    MATRIX_STR = '{0}[1m{0}[32m{{0}}{0}[0m'.format(ESC)
    MOVE_TO_TOP = '{}[0;0H'.format(ESC)
    while True:
        sys.stdout.write(MOVE_TO_TOP)
        rows, cols, x, y = getTerminalSize()
        s = (MATRIX_STR.format(getLine(cols)) for _ in range(rows))
        sys.stdout.write('\n'.join(s))
        sys.stdout.write('\r')
        sys.stdout.flush()
        time.sleep(t)

try:
    matrix()
except:
    print('')
