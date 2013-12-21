''' Cover the screen in green ones and zeroes, as if in the Matrix. '''
import time, sys
import struct, termios, fcntl
import random

ESC = '\033'

def getTerminalSize():
    ''' Get the size of the terminal.
    Return (rows, cols, x-pixels, y-pixels).
    '''
    FORMAT_STR = 'HHHH'

    s = struct.pack(FORMAT_STR, 0, 0, 0, 0)
    s = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s)
    return struct.unpack(FORMAT_STR, s)

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

if __name__ == '__main__':
    try:
        matrix()
    except:
        print('')
