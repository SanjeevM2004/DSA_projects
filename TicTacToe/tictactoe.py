class TicTacToe:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        
    def __str__(self):
        return f"{self.board[0][0]}    {self.board[0][1]}    {self.board[0][2]}\n\n\n{self.board[1][0]}    {self.board[1][1]}    {self.board[1][2]}\n\n\n{self.board[2][0]}    {self.board[2][1]}    {self.board[2][2]}"
    
    def add(self, value: str, x: int, y: int):
        if value in ['x', 'X', 'o', 'O']:
            if self.board[x][y] == '-':
                self.board[x][y] = value.upper()
            else:
                raise TypeError("Values cannot be overlapped")
        print(self)
        print(f'\nAdded {value.upper()} to position ({x}, {y})')
        win = None
        for i in range(3):
            if self.board[i] == ['X', 'X', 'X']:
                win = 'X'
            elif self.board[i] == ['O', 'O', 'O']:
                win = 'O'
        
        for j in range(3):
            value = [self.board[i][j] for i in range(3)]
            if value == ['X', 'X', 'X']:
                win = 'X'
            elif value == ['O', 'O', 'O']:
                win = 'O'
        
        value = [self.board[i][i] for i in range(3)]
        if value == ['X', 'X', 'X']:
            win = 'X'
        elif value == ['O', 'O', 'O']:
            win = 'O'
        
        value = [self.board[i][2 - i] for i in range(3)]
        if value == ['X', 'X', 'X']:
            win = 'X'
        elif value == ['O', 'O', 'O']:
            win = 'O'
        
        if win:
            return f'{win} wins!!!'
        
        if all('-' not in row for row in self.board):
            return "It's a Draw!!"
        
        return None

