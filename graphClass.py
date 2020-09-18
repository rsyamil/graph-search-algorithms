import nodeClass

class Graph:
    def __init__(self, name=[]):
        self.name = name
        self.fn_dict = {
            1 : self.act1,
            2 : self.act2,
            3 : self.act3,
            4 : self.act4,
            5 : self.act5,
            6 : self.act6,
            7 : self.act7,
            8 : self.act8,
            9 : self.act9,
            10 : self.act10,
            11 : self.act11,
            12 : self.act12,
            13 : self.act13,
            14 : self.act14,
            15 : self.act15,
            16 : self.act16,
            17 : self.act17,
            18 : self.act18
        }

    def act1(self, x, y, z):
        return str(x+1)+'-'+str(y)+'-'+str(z), 10

    def act2(self, x, y, z):
        return str(x-1)+'-'+str(y)+'-'+str(z), 10

    def act3(self, x, y, z):
        return str(x)+'-'+str(y+1)+'-'+str(z), 10

    def act4(self, x, y, z):
        return str(x)+'-'+str(y-1)+'-'+str(z), 10

    def act5(self, x, y, z):
        return str(x)+'-'+str(y)+'-'+str(z+1), 10  

    def act6(self, x, y, z):
        return str(x)+'-'+str(y)+'-'+str(z-1), 10

    def act7(self, x, y, z):
        return str(x+1)+'-'+str(y+1)+'-'+str(z), 14

    def act8(self, x, y, z):
        return str(x+1)+'-'+str(y-1)+'-'+str(z), 14      

    def act9(self, x, y, z):
        return str(x-1)+'-'+str(y+1)+'-'+str(z), 14  

    def act10(self, x, y, z):
        return str(x-1)+'-'+str(y-1)+'-'+str(z), 14    

    def act11(self, x, y, z):
        return str(x+1)+'-'+str(y)+'-'+str(z+1), 14

    def act12(self, x, y, z):
        return str(x+1)+'-'+str(y)+'-'+str(z-1), 14

    def act13(self, x, y, z):
        return str(x-1)+'-'+str(y)+'-'+str(z+1), 14 

    def act14(self, x, y, z):
        return str(x-1)+'-'+str(y)+'-'+str(z-1), 14

    def act15(self, x, y, z):
        return str(x)+'-'+str(y+1)+'-'+str(z+1), 14  

    def act16(self, x, y, z):
        return str(x)+'-'+str(y+1)+'-'+str(z-1), 14

    def act17(self, x, y, z):
        return str(x)+'-'+str(y-1)+'-'+str(z+1), 14

    def act18(self, x, y, z):
        return str(x)+'-'+str(y-1)+'-'+str(z-1), 14

    def update_neighbors(self, n):
        neighbors = []
        costs = []
        for act_idx, act in enumerate(n.action):
            id, cost = self.fn_dict[act](n.x, n.y, n.z)
            neighbors.append(id)
            costs.append(cost)
        return neighbors, costs

    def print_graph(self, graph):
        print('This is the graph: ')
        for key, value in graph.items():
            print("{} : {} : {}".format(key, value.neighbors, value.weights))

    def print_graph_parents(self, graph):
        print('This is the graph parents: ')
        for key, value in graph.items():
            print("{} : {}".format(key, value.parent_id))

    def backtrackBFS(self, graph, start_id, end_id, found_flag):

        if found_flag == False:
            return None

        total_cost = 0
        total_steps = 0
        coords_list = []
        costs_list = []

        #print('\n Backtracking \n')

        coords_list.append(end_id)
        costs_list.append(0)

        p = (graph[end_id]).parent_id
        coords_list.append(p)
        costs_list.append(1)

        while p != '-999':
            p = (graph[p]).parent_id
            coords_list.append(p)
            costs_list.append(1)

        coords_list.pop(-1)
        coords_list.reverse()

        costs_list.pop(-1) 

        total_steps = len(coords_list)
        total_cost = sum(costs_list)

        output = {
            0 : total_cost,
            1 : total_steps,
            2 : coords_list,
            3 : costs_list
        }
        return output

    def backtrackUCS(self, graph, start_id, end_id, found_flag):

        if found_flag == False:
            return None

        total_cost = 0
        total_steps = 0
        coords_list = []
        costs_list = []

        #print('\n Backtracking \n')

        coords_list.append(end_id)

        #if self.start_id == self.end_id:
        #    total_steps = 1

        p = end_id

        while p != '-999':

            p_ = (graph[p]).parent_id
            coords_list.append(p_)

            if p_ == '-999':
                break

            #get the cost to get from the parent to this end_id
            idx_child = ((graph[p_]).neighbors).index(p)
            wt_child = ((graph[p_]).weights)[idx_child]
            costs_list.append(wt_child)

            p = p_

        coords_list.pop(-1)
        coords_list.reverse()

        costs_list.append(0)
        costs_list.reverse()

        total_steps = len(coords_list)
        total_cost = sum(costs_list)

        output = {
            0 : total_cost,
            1 : total_steps,
            2 : coords_list,
            3 : costs_list
        }
        return output



      