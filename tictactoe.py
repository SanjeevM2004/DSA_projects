class TicTacToe:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        
    def __str__(self):
        return f"{self.board[0][0]}    {self.board[0][1]}    {self.board[0][2]}\n\n\n{self.board[1][0]}    {self.board[1][1]}    {self.board[1][2]}\n\n\n{self.board[2][0]}    {self.board[2][1]}    {self.board[2][2]}"
    
    def add(self, value : str, x, y):
        if value in ['x', 'X', 'o', 'O']:
            if self.board[x][y] == '-':
                self.board[x][y] = value.upper()
            else:
                raise TypeError("Values cannot be overlapped")
        print(self)
        print(F'\nAdded {value.upper()} to position ({x}, {y})')
        win = None
        value = []
        for i in range(3):
            value.append(self.board[i])
        if value == ['X', 'X', 'X']:
            win = 'X'
        elif value == ['O', 'O', 'O']:
            win = 'O'
        
        for j in range(3):
            value = []
            for i in range(3):
                value.append(self.board[i][j])
            if value == ['X', 'X', 'X']:
                win = 'X'
            elif value == ['O', 'O', 'O']:
                win = 'O'
        for i in range(3):
            value.append(self.board[i][i])
        if value == ['X', 'X', 'X']:
                win = 'X'
        elif value == ['O', 'O', 'O']:
            win = 'O'
        value = []
        if value == 1:
            win = 'O'
        value=[]
        for i in range(3):
            value.append(self.board[i][abs(i-2)])
        if value == ['X', 'X', 'X']:
            win = 'X'
        elif value == ['O', 'O', 'O']:
            win = 'O'
        if win != None:
            return f'{win} wins!!!'   
        
        value = []
        for i in range(3):
            if '-' not in self.board[i] and win == None:
                value.append(1)
            else:
                value.append(0)
                
        if 0 in value:
            pass
        else:      
            return "It's a Draw!!"

board = TicTacToe()
#Use this command below for adding X/O to that particular coordinate.
board.add('X', 0, 0)
        