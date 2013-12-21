'''
A game where the user and computer take turns erasing either
1 or 2 lines. Whoever erases the last line loses.  The user
and computer take turns going first.  Loser is 1 mod 3.
'''

from random import randint

games = wins = losses = 0

def newGame():
    lines = 22
    print('Game started.')
    printLines(lines)
    if games % 2 == 0: playerTurn(lines)
    else: compTurn(lines, 1)

def playerTurn(lines):
    erasedLines = getInput()
    lines -= erasedLines
    print('You erased {} lines!\n'.format(erasedLines))
    printLines(lines)

    gameOver('p') if lines < 1 else compTurn(lines, erasedLines)

def compTurn(lines, lastMove):
    erasedLines = (lines - 1) % 3
    if erasedLines == 0:
        erasedLines = randint(1, 2)
    lines -= erasedLines
    print('The computer erased {} lines!\n'.format(erasedLines))
    printLines(lines)
    gameOver('c') if lines < 1 else playerTurn(lines)

def printLines(n):
    if n <= 0:
        print('There are no lines left!');
    elif n == 1:
        print('There is 1 line left!')
        print('|')
    else:
        print('There are {} lines left!'.format(n))
        print('|' * n)

def getInput():
    VALID_NUMBERS = '12'
    HELP_STRINGS = ('help', '?')
    EXIT_STRINGS = ('exit', 'quit')
    HELP = ('\nPlease enter a 1 or a 2. Type "help" for help or '
            '"exit" to exit.\n')

    while True:
        s = input('How many lines would you like to erase? ').lower()
        if not s: continue

        if s in VALID_NUMBERS:
            return int(s)
        elif s in HELP_STRINGS:
            printRules();
        elif s in EXIT_STRINGS:
            sys.exit(0)
        else:
            print(HELP)

def gameOver(l):
    SCOREBOARD = (
        '\nSCOREBOARD\n'
        'Games:  {0}\n'
        'Wins:   {1}\n'
        'Losses: {2}\n'
    )
    global games, losses, wins
    games += 1
    if l == 'p':
        losses += 1
        print('You lost.  Better luck next time!')
    else:
        wins += 1
        print('You won!  Good job!')
    print(SCOREBOARD.format(games, wins, losses))
    newGame()

def printRules():
    h = ('The rules are simple: every turn, you get to erase either 1 or\n'
        '2 lines. The last person to erase a line loses. You and the\n'
        'computer will take turns going first, so that nobody is left at\n'
        'an unfair advantage.')
    print('\nHelp:\n')
    print(h)

if __name__ == '__main__':
    newGame()
