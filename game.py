board_template = ['','','','','','','','','']
turn = [True, False]
def displayBoard(board = []):
    for index in xrange(0,9):
        if board[index] == '':
            print '|-|',
            if index in range(2, 7, 3):
                print '\n',
        else:
            print '|' + board[index] + '|',
            if index in range(2, 7, 3):
                print '\n',


def getPlayerTurn(turn_list):
    if turn_list[0] == True:
        return 'Player 1'
    else:
        return 'Player 2'

def reverseTurn(turn_list):
    if turn_list[0] == True:
        return [False, True]
    else:
        return [True, False]

def getPlayerMark(turn_list):
    if turn_list[0] == True:
        return 'X'
    else:
        return 'O'

def checkWinner(board_template):
    # Check Rows
    if board_template[0] == 'X' and board_template[1] == 'X' and board_template[2] == 'X':
        return 'Player 1'
    elif board_template[3] == 'X' and board_template[4] == 'X' and board_template[5] == 'X':
        return 'Player 1'
    elif board_template[6] == 'X' and board_template[7] == 'X' and board_template[8] == 'X':
        return 'Player 1'
    elif board_template[0] == 'O' and board_template[1] == 'O' and board_template[2] == 'O':
        return 'Player 2'
    elif board_template[3] == 'O' and board_template[4] == 'O' and board_template[5] == 'O':
        return 'Player 2'
    elif board_template[6] == 'O' and board_template[7] == 'O' and board_template[8] == 'O':
        return 'Player 2'
    # Check Columns
    elif board_template[0] == 'X' and board_template[3] == 'X' and board_template[6] == 'X':
        return 'Player 1'
    elif board_template[1] == 'X' and board_template[4] == 'X' and board_template[7] == 'X':
        return 'Player 1'
    elif board_template[2] == 'X' and board_template[5] == 'X' and board_template[8] == 'X':
        return 'Player 1'
    elif board_template[0] == 'O' and board_template[3] == 'O' and board_template[6] == 'O':
        return 'Player 2'
    elif board_template[1] == 'O' and board_template[4] == 'O' and board_template[7] == 'O':
        return 'Player 2'
    elif board_template[2] == 'O' and board_template[5] == 'O' and board_template[8] == 'O':
        return 'Player 2'
    # Check Diagonals
    elif board_template[0] == 'X' and board_template[4] == 'X' and board_template[8] == 'X':
        return 'Player 1'
    elif board_template[2] == 'X' and board_template[4] == 'X' and board_template[6] == 'X':
        return 'Player 1'
    elif board_template[0] == 'O' and board_template[4] == 'O' and board_template[8] == 'O':
        return 'Player 2'
    elif board_template[2] == 'O' and board_template[4] == 'O' and board_template[6] == 'O':
        return 'Player 2'
    else:
        return False

def runGame(board_template, turn):
    tie = True
    for block in board_template:
        if block == '':
            tie = False
    winner = False
    displayBoard(board_template)
    if tie == True:
        print '\nIt\'s a tie!'
        prompt = raw_input('Would you like to try again? Y/N')
        if prompt == 'Y':
            iteration = 0
            for i in xrange(0, 9):
                board_template[i] = ''
            runGame(board_template, [True, False])
        else:
            exit()
    print '\n'
    player_raw_input = int(input('%s\'s turn(1 - 9): ' % (getPlayerTurn(turn)))) - 1
    if board_template[player_raw_input] != '':
        runGame(board_template, turn)
    board_template[player_raw_input] = getPlayerMark(turn)
    turn = reverseTurn(turn)
    winner = checkWinner(board_template)
    if winner == False:
        runGame(board_template, turn)
    else:
        displayBoard(board_template)
        print '\n%s won!' %(winner)
        prompt = raw_input('Would you like to try again? Y/N\nAnswer: ')
        if prompt == 'Y' or prompt == 'y':
            iteration = 0
            for i in xrange(0, 9):
                board_template[i] = ''
            runGame(board_template, [True, False])
        else:
            exit()

runGame(board_template, turn)