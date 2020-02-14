def display_board(board):
    """显示棋盘"""
    print("\t{0} | {1} | {2}".format(board[0], board[1], board[2]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[3], board[4], board[5]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[6], board[7], board[8]))


def legal_moves(board):
    """返回可落子的位置列表"""
    moves = []#存放的是int类型
    for i in range(9):
        if board[i] in list("012345678"):
            moves.append(i)
    return moves


def getPlayerMove(board):
    """询问并确定玩家的选择落子位置，无效位置时重复询问"""
    move = 9
    while move not in legal_moves(board):
        move = int(input("请选择落子位置（0-8）："))
    return move


def getComputerMove(board, computerLetter, playerLetter):
    """核心算法：计算人工智能AI的落子位置"""
    boardcopy = board.copy()

    # 规则一：判断如果某位置落子可以获胜，则选择该位置
    for move in legal_moves(boardcopy):
        boardcopy[move] = computerLetter
        if isWinner(boardcopy):
            return move
        boardcopy[move] = str(move)
    
    # 规则二：某个位置玩家下一步落子可以获胜，则选择该位置
    for move in legal_moves(boardcopy):
        boardcopy[move] = playerLetter
        if isWinner(boardcopy):
            return move
        boardcopy[move] = str(move)
    
    # 规则三：按照中心、角、边的顺序选择空的位置
    for move in (4,0,2,6,8,1,3,5,7):
        if move in legal_moves(board):
            return move

        
def isWinner(board):
    """判断所给的棋子是否获胜"""
    WAYS_TO_WIN = {(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)}
    for r in WAYS_TO_WIN:
        if board[r[0]] == board[r[1]] == board[r[2]]:
            return True
    return False


def isTie(board):
    """判断是否平局"""
    for i in list("012345678"):
        if i in board:
            return False
    return True


def tic_tac_toe():
    """井字棋"""
    board = list("012345678")
    playerLetter = input("请选择棋子X或者O（X先走，O后走）：")
    if playerLetter in ("X", "x"):
        turn = "player"
        playerLetter = "X"
        computerLetter = "O"
    else:
        turn = "computer"
        computerLetter = "X"
        playerLetter = "O"
    print("{}先走！".format(turn))

    while True:
        display_board(board)
        if turn == 'player':
            move = getPlayerMove(board)
            board[move] = playerLetter
            if isWinner(board):
                display_board(board)
                print("恭喜玩家获胜！")
                break
            else:
                turn = "computer"
        else:
            move = getComputerMove(board, computerLetter, playerLetter)
            print("计算机人工智能AI落子位置：", move)
            board[move] = computerLetter
            if isWinner(board):
                display_board(board)
                print("计算机人工智能AI获胜！")
                break
            else:
                turn = "player"

        if isTie(board):
            display_board(board)
            print('平局！！！')
            break


if __name__ == '__main__':
    tic_tac_toe()

