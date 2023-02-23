import numpy as np
column=7
row=6
def board_struct():
    board=np.zeros((row,column))
    return board
def drop(selection,board,player_no):
    position=0
    for i in range(board.shape[0]-1,-1,-1):
        if(board[i][selection] == 0):
            position=i
            break
    board[position][selection]=player_no
    return board
def is_valid_location(board,col):
    return(board[0][col]==0)
def wining_move(piece ,board):
    #check horizontal 
    for c in range(column-3):
        for r in range(row):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                    return True 
    #check vertical
    for c in range(column):
        for r in range(row-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                    return True
    
    for c in range(column-3):
        for r in range(row-1,2,-1):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                    return True 
    for c in range(column-3):
        for r in range(row-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                    return True 
            
board=board_struct()
game_over=False
turn=0
while not game_over:
    if turn%2==0:
        selection=int(input("player 1 make your choice (0-6):"))
        valid=is_valid_location(board,selection)
        if(valid):
            board=drop(selection,board,1)
        else:
            print("try again")
            pass
        if(wining_move(board=board,piece=1)):
            print("Player 1 wins")
            break
    else:
        selection=int(input("player 2 make your choice (0-6):"))
        valid=is_valid_location(board,selection)
        if(valid):
            board=drop(selection,board,2)
        else:
            print("Try again")
            pass
        if(wining_move(board=board,piece=2)):
            print("Player 2 wins")
            break
    print(board)
    turn+=1
