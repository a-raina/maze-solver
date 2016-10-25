'''
Anmol Raina
25th Oct. 2016
'''

from maze_backend import Maze

'''
To run, initialize a matrix and create a Maze object as shown below. You can then call the algorithms on the matrices.
Currently, I assume (0,0) to be the startingpoint and (len(matrix)-1,len(matrix[0])-1) to be the ending point, symbolized
by 'A' and 'B' respectively.

Please enter valid input. A and B can be 0s instead.
'''

#matrix = [['A',0,1,1,1,1], [1,0,0,0,0,1], [1,1,0,1,0,0], [1,0,0,1,1,0], [1,1,0,0,0,'B'] ]
matrix =[['A', 0,0,0], [1,1,0,0],[1,0,0,0],  [1,0,1,0], [1,0,0,'B']] 
maze = Maze(matrix)
maze.bfs_solution()
maze.aStar_solution()

