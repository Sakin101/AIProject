import numpy as np
def board_struct():
    board=np.zeros((6,7))
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
def get_next_open_row():
    pass
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
    else:
        selection=int(input("player 2 make your choice (0-6):"))
        valid=is_valid_location(board,selection)
        if(valid):
            board=drop(selection,board,2)
        else:
            print("Try again")
            pass
    print(board)
    turn+=1
