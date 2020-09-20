#######
# Functions to extract information to be displayed from .txt files
# many functions overlap with parserClass.py
# input.txt -> to initialize the display
# steps.txt -> intermediate steps taken during traversal
# output.txt -> the final path found as the solution
#######

def input_file_parser():
    with open('input.txt') as file:

        #placeholder for list of nodes
        nodes_x = []
        nodes_y = []
        nodes_z = []

        #read the algorithm type, string [BFS][UCS][A*]
        alg = (file.readline()).rstrip("\n")
        print('Using algorithm :\t {}'.format(alg))

        #read the bounding box integers x, y, and z
        bbox_dim = [int(s) for s in file.readline().split() if s.isdigit()]
        print('Dimension of maze is :\t {}x{}x{}'.format(bbox_dim[0], bbox_dim[1], bbox_dim[2]))

        #read the coordinate of the starting point (integers list)
        start_coord = [int(s) for s in file.readline().split() if s.isdigit()]

        #read the coordinate of the ending point (integers list)
        end_coord = [int(s) for s in file.readline().split() if s.isdigit()]

        #read the next N lines of possible coords and actions
        num_lines = int(file.readline())
        for line in range(num_lines):
            vals = [int(s) for s in file.readline().split() if s.isdigit()]
            nodes_x.append(vals[0])
            nodes_y.append(vals[1])
            nodes_z.append(vals[2])


    return alg, bbox_dim, start_coord, end_coord, nodes_x, nodes_y, nodes_z

def output_file_parser():
    with open('output.txt') as file:

        #placeholder for list of nodes
        nodes_x = []
        nodes_y = []
        nodes_z = []

        #cost of the algorithm
        cost = int(file.readline())

        #number of steps taken 
        steps = int(file.readline())

        #read all the coordinates of the solution path
        for line in range(steps):
            vals = [int(s) for s in file.readline().split() if s.isdigit()]
            nodes_x.append(vals[0])
            nodes_y.append(vals[1])
            nodes_z.append(vals[2])

    return cost, steps, nodes_x, nodes_y, nodes_z


