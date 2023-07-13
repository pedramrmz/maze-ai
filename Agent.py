import collections
from operator import attrgetter
import colorsys
from turtle import position
from Environment import Board
import pygame


class Agent:
    board:Board
    def __init__(self, board):
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()
        self.bfs_intricacy = 0
        self.dfs_intricacy = 0
        self.aStar_intricacy = 0
        self.board = board
        self.position = board.get_agent_pos()
   


    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        self.current_state = board.get_current_state()

        pass

    @staticmethod
    def get_actionss():
        actions = []
        # returns a list of valid actions
        return actions

    def set_position_dfs(self, position, board):
        self.position = position
        board.set_agent_pos_dfs(position)
        board.update_board(self.current_state)

    def move_dfs(self,i,j):
        self.set_position_dfs([i,j] ,self.board)

    def move(self, direction):
       
        self.set_position(self.get_position() + direction)

    

    def dfs(self,c,env,w):

        # clock = pygame.time.Clock()
        env.draw_world(w)
        c.tick(30)
        current_pos = self.get_position()
        if not self.board.valid_position(current_pos) or \
            self.board.IsVisited(current_pos) or \
            self.board.IsWall(current_pos):
           # self.dfs_intricacy += 1
            return False
        
        if(self.board.isGolal(current_pos)):
            print("dfs intricacy =")
            print(int(self.dfs_intricacy))
            return True

        self.board.SetVisited(current_pos)
        neighbors = self.board.GetNeighberhoods(current_pos[0],current_pos[1])

        for ni, nj, wall in neighbors:
            self.dfs_intricacy += 1/2 
            if self.board.valid_position([ni, nj]) == True and \
               not wall  \
               and self.board.IsVisited([ni, nj]) == False:
                self.move_dfs(ni,nj)
                if self.dfs(c,env,w):
                   
                    return True
       
    
    def get_actions(self, x, y):
        actions = []
        
        if x + 1 < 13:
            if not self.current_state[x + 1][y].isBlocked:
                actions.append(self.current_state[x + 1][y])
        if x - 1 > -1:
            if not self.current_state[x - 1][y].isBlocked:
                actions.append(self.current_state[x - 1][y])
        if y + 1 < 13:
            if not self.current_state[x][y + 1].isBlocked:
                actions.append(self.current_state[x][y + 1])
        if y - 1 > -1:
            if not self.current_state[x][y - 1].isBlocked:
                actions.append(self.current_state[x][y - 1])
        return actions


    def bfs(self, environment, start):
        
        
        all_node=169
        search_node=13
        bfsPath = {}
        open_List_node = [start]
        
        close_List_node = set()
        close_List_node.add(start)
        search_node=search_node-1
        while len(open_List_node) is not 0:
            self.add_countt()
            present_node = open_List_node.pop(0)
            if present_node.isGoal:
                self.painting(environment, bfsPath\
                              , '#66CDAA', 'bfs', self.bfs_intricacy)
                break
            for action in self.get_actions(present_node.x, present_node.y):
                if action not in close_List_node:
                    self.regularize_list(open_List_node, close_List_node, action)
                    bfsPath.update({(action.x, action.y):
                                     (present_node.x, present_node.y)})

    def regularize_list(self, open_List_node, close_List_node, action):
        close_List_node.add(action)
        open_List_node.append(action)

    def add_countt(self):
        self.bfs_intricacy= 1+self.bfs_intricacy


    


    def a_star(self, environment, start):
        
        open_List_node = [start]
        close_List_node = set()
        close_List_node.add(start)
        a_star_Path = {}
        while len(open_List_node) is not 0:
            self.aStar_intricacy = self.aStar_intricacy+1
            present_node = self.find_min(open_List_node)
            open_List_node.remove(present_node)
           
          
            if present_node.isGoal:
                self.paint_road(environment, a_star_Path)
                break
            for action in self.get_actions(present_node.x, present_node.y):
                if action not in close_List_node:
                    action.function_astar(present_node.get_cost() + 1)
                    close_List_node.add(action)
                    open_List_node.append(action)
                    a_star_Path.update({(action.x, action.y):
                    (present_node.x, present_node.y)})

    def find_min(self, open_List_node):
        present_node = min(open_List_node, key=attrgetter('f'))
        return present_node

    def paint_road(self, environment, a_star_Path):
        self.painting(environment, a_star_Path,\
                               '#FFD39B', 'a_star', self.aStar_intricacy)
                                    
    def painting(self, environment, path, color, name, intricacy):
        self.bfs_intricacy = 0
        self.dfs_intricacy = 0
        self.aStar_intricacy = 0
        pathLength = 0
        coloring = path[(12, 0)]
        
        while path.get(coloring):
           
            environment.painting(coloring[0], coloring[1], color)
            pathLength =pathLength+ 1
            coloring = path.get(coloring)
        self.bestt_road(name, pathLength)
        self.print_result(name, intricacy)

    def bestt_road(self, name, pathLength):
        print(f'best road {name} =\n {pathLength + 1}')

    def print_result(self, name, intricacy):
        print(f'{name} intricacy =\n {intricacy}')
        
