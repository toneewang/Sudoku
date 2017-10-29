import math

class SudokuBoard:
    def __init__(self,board):
        self._board = board

    '''
    需要显示的内容
    '''
    def __str__(self):
        result = ""
        for i in range(9):
            for k in range(9):
                if self.get(k,i) == 0:
                    result += " "
                else:
                    result += str(self.get(k,i))
                    result += ""
            result += "\n"
        return result

    '''
    输入x,y轴坐标，从数组中取值
    '''
    def get(self,x,y):
        return self._board[y][x]

    '''
    输入x,y轴坐标及值，将值输入
    '''
    def set(self,x,y,val):
        self._board[y][x] = val

    def erase(self,x,y):
        self._board[x][y] = 0

    def check(self,x,y):
        num = self.get(x,y)
        h_num = []
        for i in range(9):
            if i != x:
                h_num.append(self.get(i,y))
        if num in h_num : return False
        v_num = []
        for i in range(9):
            if i != y:
                h_num.append(self.get(i,y))
        if num in v_num : return False
        return True

    def next(self):
        for i in range(9):
            for k in range(9):
                if self.get(k,i) == 0:
                    return (k,i)
        return False
