from board import SudokuBoard


def accept(board):
    if board.next == False:
        return True
    return False

def solve(board):
    if accept(board):return True
    (x,y) = board.next
    for i in range(1,10):
        board.set(x,y,i)
        if board.check(x,y):
            if solve(x,y) == True:return True
        board.erase(x,y)
    return False

if __name__ == '__main__':
    board = SudokuBoard([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
    print(board)
    solve(board)
    print(board)