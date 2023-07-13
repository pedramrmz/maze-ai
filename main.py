import copy
import pygame
import colors
from params import *
from Environment import Board
from Agent import Agent

# initialize:
user_input = int(input("enter your number between 1-3 to find goal\n 1)Deap-First-Search(dfs)\
                        \n 2)Breadth-First-Search(bfs) \n 3)A* Search :\n   "))
FPS = 3
flag = True
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Search Game")

# setting start and end point :
start = {'x': 6, 'y': 0}
end = {'x': 12, 'y': 0}

gameBoard = Board(start, end)
agent = Agent(gameBoard)
gameBoard_copy = copy.deepcopy(gameBoard)


def main(user_input):
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors.black)
    flag = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gameBoard.draw_world(WIN)
        pos = pygame.mouse.get_pos()  # gets the current mouse coords

        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
            for i in range(rows):
                for j in range(cols):
                    if not gameBoard.boardArray[i][j].isBlocked and not \
                        gameBoard.boardArray[i][j].isStart\
                            and not gameBoard.boardArray[i][j].isGoal:
                        gameBoard.boardArray[i][j].restore_color()
                    rect = gameBoard.boardArray[i][j]
                    if rect.is_inside_me(pos):

                        if event.button == 1:
                            gameBoard.boardArray[i][j].block()
                        if event.button == 3:
                            gameBoard.boardArray[i][j].unblock()

#####
        if flag:
                match user_input:
                        case 1:
                            agent.dfs(clock,gameBoard,WIN)
                            pygame.display.set_caption('Deap-First-Search')
                        case 2:
                            agent.bfs(gameBoard, gameBoard.boardArray[6][0])
                            pygame.display.set_caption('Breadth-First-Search')  
                        case 3:
                            agent.a_star(gameBoard, gameBoard.boardArray[6][0])
                            pygame.display.set_caption('A Star')
                

   
main(user_input)
