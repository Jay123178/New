def sudoko(board):
    def isvalid(board,row,col,unqnum):
        for i in  range(0,9):
            if board[row][i]== unqnum or board[i][col]==unqnum:
                return False
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3 ] == unqnum:
                return False
        return True
    
    def solve(board):
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] == 0:
                    for unqnum in range(1,10):
                        if isvalid(board,row,col,unqnum):
                            board[row][col]= unqnum
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    solve(board)
    return board

board=[
     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]

]

solved = sudoko(board)

for row in solved:
    print(row)


