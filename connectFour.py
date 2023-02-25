import numpy as np
import pygame
import sys
import math
blue=(0,0,255)
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
def draw_board(board):
    for c in range(column):
        for r in range(row):
            pygame.draw.rect(screen,blue,(c*pixel_size,r*pixel_size+pixel_size,pixel_size,pixel_size))
            if board[r][c]==0:
                pygame.draw.circle(screen,(0,0,0),(c*pixel_size+radius,r*pixel_size+pixel_size+radius),radius)
            if board[r][c]==1:
                pygame.draw.circle(screen,(255,0,0),(c*pixel_size+radius,r*pixel_size+pixel_size+radius),radius)
            elif board[r][c]==2:
                pygame.draw.circle(screen,(255,255,0),(c*pixel_size+radius,r*pixel_size+pixel_size+radius),radius)
board=board_struct()
game_over=False
turn=0
pygame.init()
myfont=font = pygame.font.SysFont('monospace', 60)
pixel_size=100
radius=int(pixel_size/2)
width=pixel_size*column
height=pixel_size*(row+1)

size=(width,height)

screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if turn%2==0:
                posx=event.pos[0]
                col=int(math.floor(posx/pixel_size))
                
                selection=col
                valid=is_valid_location(board,selection)
                if(valid):
                    board=drop(selection,board,1)
                else:
                    print("try again")
                    pass
                if(wining_move(board=board,piece=1)):
                    label=myfont.render("Player 1 wins",1,(255,0,0))
                    screen.blit(label,(40,10))
                    game_over=True
            else:
                posx=event.pos[0]
                col=int(math.floor(posx/pixel_size))
                selection=col
                valid=is_valid_location(board,selection)
                if(valid):
                    board=drop(selection,board,2)
                else:
                    print("Try again")
                    pass
                if(wining_move(board=board,piece=2)):
                    label=myfont.render("Player 2 wins",1,(255,0,0))
                    screen.blit(label,(40,10))
                    game_over=True
            turn+=1
    print(board)
    draw_board(board)
        
    pygame.display.update()
    if game_over:
        pygame.time.wait(3000)
    
