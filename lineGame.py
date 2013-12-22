'''
A game where the user and computer take turns erasing either
1 or 2 lines. Whoever erases the last line loses.  The user
and computer take turns going first.
'''

import sys
from random import randint
from collections import defaultdict

def playGame():
    ''' Wrapper to play a whole game. '''
    SCOREBOARD = (
        '\nSCOREBOARD\n'
        'Games:  {games}\n'
        'Wins:   {wins}\n'
        'Losses: {losses}\n'
    )
    stats = defaultdict(int)
    while True:
        playerWon = playRound(stats['games'])
        stats['wins'] += playerWon
        stats['games'] += 1
        stats['losses'] = stats['games'] - stats['wins']
        print(SCOREBOARD.format(**stats))

def playRound(games):
    ''' Wrapper to play a round. '''
    WIN_MESSAGE = 'You won!'
    LOSE_MESSAGE = 'You lost. Better luck next time.'
    lines = 22
    turn = games % 2
    players = (computerTurn, playerTurn)

    print('Round started.')

    # Decide who goes first
    while True:
        # Function to call to play
        play = players[turn % 2]
        printLines(lines)
        # Play the turn and subtract the move
        lines -= play(lines)

        # Whose turn it is
        turn = (turn + 1) % 2

        if lines <= 0:
            # Round is over
            message = WIN_MESSAGE if turn else LOSE_MESSAGE
            print(message)
            return turn

def playerTurn(lines):
    ''' Human turn. '''
    move = getInput()
    print('You erased {} lines!'.format(move))
    return move

def computerTurn(lines):
    ''' Computer plays a turn. '''
    # We want to always force the player to play on n == (1 mod 3)
    move = (lines - 1) % 3
    if move == 0:
        move = randint(1, 2)
    print('The computer erased {} lines!\n'.format(move))
    return move

def printLines(n):
    ''' Print the lines. '''
    if n <= 0:
        print('There are no lines left!');
    elif n == 1:
        print('There is 1 line left!')
        print('|')
    else:
        print('There are {} lines left!'.format(n))
        print('|' * n)

def getInput():
    VALID_NUMBERS = ('1', '2')
    HELP_STRINGS = ('help', '?')
    EXIT_STRINGS = ('exit', 'quit')
    HELP = ('\nPlease enter a 1 or a 2. Type "help" for help or '
            '"exit" to exit.\n')

    while True:
        s = input('How many lines would you like to erase? ').lower()

        if s in VALID_NUMBERS:
            return int(s)
        elif s in HELP_STRINGS:
            printRules();
        elif s in EXIT_STRINGS:
            sys.exit(0)
        else:
            print(HELP)

def printRules():
    h = ('The rules are simple: every turn, you get to erase either 1 or\n'
        '2 lines. The last person to erase a line loses. You and the\n'
        'computer will take turns going first, so that nobody is left at\n'
        'an unfair advantage.')
    print('\nHelp:\n')
    print(h)

if __name__ == '__main__':
    try:
        playGame()
    except KeyboardInterrupt as e:
        print('')
        sys.exit(0)
