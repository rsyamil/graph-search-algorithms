from collections import deque
import pickle

class DFS:
    def __init__(self, name=[], graph=0, start_id=0, end_id=0):
        self.name = name
        self.graph = graph
        self.start_id = start_id
        self.end_id = end_id
        self.found_flag = False

    def run_dfs(self):

        ############
        #the length of both list is max of number of vertices
        #each element will not have the same length
        iter_visited_x = []
        iter_visited_y = []
        iter_queued_x = []
        iter_queued_y = []
        ############

        explored = set()
        queue = deque([self.start_id])

        #corner case
        if self.start_id == self.end_id:
            print('\n Start == End \n')
        
        while queue:

            #print("Current queue : ", queue)
            v = queue.pop()
            #print("Current vertex : ", v)
            
            if v not in explored:

                neighbours = (self.graph[v]).neighbors
                #print(neighbours)
                
                for n in neighbours:

                    #check feasibility of movements
                    if n not in self.graph:
                        continue

                    if n not in explored:
                        (self.graph[n]).parent_id = v
                        queue.append(n)
                
                explored.add(v)

                ############
                temp_x = []
                temp_y = []
                for e in explored:
                    temp_x.append((self.graph[e]).x)
                    temp_y.append((self.graph[e]).y)
                iter_visited_x.append(temp_x)
                iter_visited_y.append(temp_y)
                ############

                ############
                temp_x = []
                temp_y = []
                for e in queue:
                    temp_x.append((self.graph[e]).x)
                    temp_y.append((self.graph[e]).y)
                iter_queued_x.append(temp_x)
                iter_queued_y.append(temp_y)
                ############
                
                if (v == self.end_id):
                    print('\n Found \n')

                    ############
                    with open("explored_x.txt", "wb") as fp:
                        pickle.dump(iter_visited_x, fp)
                    with open("explored_y.txt", "wb") as fp:
                        pickle.dump(iter_visited_y, fp)

                    with open("queued_x.txt", "wb") as fp:
                        pickle.dump(iter_queued_x, fp)
                    with open("queued_y.txt", "wb") as fp:
                        pickle.dump(iter_queued_y, fp)
                    ############

                    self.found_flag = True
                    return self.found_flag

        return self.found_flag
    
