from colorama import init, Fore, Back, Style
from aStar import *

init(autoreset=True)

'''
Given a matrix of 1s and 0s, find the shortest route between two points in the matrix while considering 1s as walls and 0s as traversable paths. 
'''

class Maze:
    maze = []
    def __init__(self, matrix):
        self.maze = matrix
        
    '''
    helper function to the backtracking algorithm 
    i=starting row
    j=starting column
    end=tuple, holding the ending row and column
    path=array of coordinates on the path
    visited=coordinates visited so far
    '''
    def __find_shortest_route(self, i, j, end, path, visited):
        if (i,j) in visited:
            return False
        if i<0 or i> len(self.maze)-1 or j<0 or j>len(self.maze[0])-1:
            return False
        if self.maze[i][j] == 1:
            return False
        visited[(i,j)] = None
        if (i, j) == end:
            path.append((i,j))
            return True
        path.append((i,j))
        if(self.__find_shortest_route(i, j+1, end, path, visited)):
            return True
        if(self.__find_shortest_route(i-1, j, end, path, visited)):
            return True
        if(self.__find_shortest_route(i, j-1, end, path, visited)):
            return True
        if(self.__find_shortest_route(i+1, j, end, path, visited)):
            return True
        return False
    
    '''
    BFS backtracking solution
    (does not find the shortest path)
    Time Complexity: O(nm), where n = # of rows, m = # of columns
    '''
    def bfs_solution(self, start=(0,0), end=(0,0)):
        end=(len(self.maze)-1, len(self.maze[0])-1)
        visited = {}
        path = []
        if(not self.__find_shortest_route(start[0], start[1], end, path, visited)):
            raise ValueError('No Path Found')
#        path.sort()
        print("BFS backtracking solution: ", path)
        dict_path = {}
        for i in path:
            dict_path[i] = None
        self.__draw_solution(path, dict_path)

        
    '''
    A* solution
    (finds the shortest path)
    Time Complexity: O(n), where n = # nodes in the path
    '''
    def aStar_solution(self,start=(0,0), end=(0,0)):
        end=(len(self.maze)-1, len(self.maze[0])-1)
        start = (0,0)
        tempMaze = []
        #creating a temporary copy so I don't change the original matrix
        for row in range(len(self.maze)):
            temp = []
            for column in range(len(self.maze[row])):            
                temp.append(self.maze[row][column])
            tempMaze.append(temp)
        #calls the controller function in aStar.py, which returns a path
        path = controller(tempMaze, start, end)
        print("A* solution: ", path)
        dict_path = {}
        for i in path:
            dict_path[i] = None
        self.__draw_solution(path, dict_path)
        
    '''
    Helper method to turn the nodes on the path green
    '''
    def __draw_solution(self, path, dict_path):
        for row in range(len(self.maze)):
            for column in range(len(self.maze[row])):
                if (row,column) in dict_path:
                    print(Back.GREEN + str(self.maze[row][column]), end="")
                else:
                    print(self.maze[row][column], end="")
            print()

        
        