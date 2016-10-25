'''
Code to implement the A* algorithm. 
The cost function currently returns 0 as we do not favor a certain node over the other. If 
we wanted to visit certain Nodes we could give those nodes low cost and others higher cost.
'''

class Node:
    def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
    def move_cost(self,other):
        return 0
        
'''
returns adjacent Nodes
'''
def children(point,grid):
    x,y = point.point
    neighbours = []
    if x-1 >= 0:
        neighbours.append((x-1, y))
    if y-1 >= 0:
        neighbours.append((x,y - 1))
    if y+1 < len(grid[0]):
        neighbours.append((x,y + 1))
    if x+1 < len(grid):
        neighbours.append((x+1,y))
    links = [grid[d[0]][d[1]] for d in neighbours]
    return [link for link in links if link.value !=  1]

'''
calculates the manhattan distance between two points
'''
def manhattan(point,point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])

'''
main A* algorithm
'''
def aStar(start, goal, grid):
    #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the starting point
    current = start
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #If it is the item we want, retrace the path and return it
#        print(current.point)
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings
        for node in children(current,grid):
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')
    

#Convert all the points to instances of Node
def convert_matrix_to_grid(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] = Node(matrix[x][y],(x,y))
    return matrix
        
#main function that calls everything
def controller(matrix,start, end):
    grid = convert_matrix_to_grid(matrix)
    path = aStar(grid[start[0]][start[1]],grid[end[0]][end[1]],grid)  
    returnPath = []
    for node in path:
        x, y = node.point
        returnPath.append((x,y))
    return returnPath
    

