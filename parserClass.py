import string
import nodeClass

class Parser:

    def __init__(self, name='Parser'):
        self.name = name

    def file_parser(self):
        with open('input.txt') as file:

            #placeholder for list of nodes
            nodes = []

            #read the algorithm type, string [BFS][UCS][A*]
            alg = (file.readline()).rstrip("\n")
            print('Using algorithm :\t {}'.format(alg))

            #read the bounding box integers x, y, and z
            bbox_dim = [int(s) for s in file.readline().split() if s.isdigit()]
            print('Dimension of maze is :\t {}x{}x{}'.format(bbox_dim[0], bbox_dim[1], bbox_dim[2]))

            #read the coordinate of the starting point (integers list)
            start_coord = [int(s) for s in file.readline().split() if s.isdigit()]
            print('Start coordinate :\t ({}, {}, {})'.format(start_coord[0], start_coord[1], start_coord[2]))
            start_id = str(start_coord[0])+'-'+str(start_coord[1])+'-'+str(start_coord[2])

            #read the coordinate of the ending point (integers list)
            end_coord = [int(s) for s in file.readline().split() if s.isdigit()]
            print('End coordinate :\t ({}, {}, {})'.format(end_coord[0], end_coord[1], end_coord[2]))
            end_id = str(end_coord[0])+'-'+str(end_coord[1])+'-'+str(end_coord[2])

            #read the next N lines of possible coords and actions
            num_lines = int(file.readline())
            for line in range(num_lines):
                vals = [int(s) for s in file.readline().split() if s.isdigit()]
                newNode = nodeClass.Node(vals[0], vals[1], vals[2], vals[3:])
                nodes.append(newNode)

        return alg, bbox_dim, start_id, end_id, nodes

    def file_writer(self, output, graph, found_flag):
        with open('output.txt', 'w') as file:

            if found_flag == True:
                file.write(str(output[0])+'\n')
                file.write(str(output[1])+'\n')

                coords_list = output[2]
                costs_list = output[3]

                for i in range(len(coords_list)):
                    file.write(str((graph[coords_list[i]]).x)+' ')
                    file.write(str((graph[coords_list[i]]).y)+' ')
                    file.write(str((graph[coords_list[i]]).z)+' ')
                    file.write(str(costs_list[i]))

                    if i != (len(coords_list)-1):
                        file.write('\n')
            else:
                file.write('FAIL')



                