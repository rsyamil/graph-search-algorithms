######
# Important implementation note: https://en.wikipedia.org/wiki/A*_search_algorithm
# Once a node is in the explored set, and later reached by a shorter parth, it needs to 
# be added to the frontier again. This is important when heuristic is admissible but not 
# consistent. If the h(n) is admissible + consistent, anytime you remove a node from the 
# frontier, it is guaranteed to be optimal - so there is no need to add it to the 
# frontier again. 
######

import pqClass
import math
import pickle

def euclidean_distance(v1, v2):
    return 9.0*round(math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2), 1)

def manhattan_distance(v1, v2):
    return math.sqrt(abs(v1.x - v2.x) + abs(v1.y - v2.y) + abs(v1.z - v2.z))

class ASTAR:
    def __init__(self, name=[], graph=0, start_id=0, end_id=0):
        self.name = name
        self.graph = graph
        self.start_id = start_id
        self.end_id = end_id
        self.found_flag = False

    def update_heuristic(self, h='Euclidean'):

        if self.end_id not in self.graph:
            print('\n End-point does not exist \n')
            return

        if h == 'Euclidean':
            for n_id in self.graph:
                (self.graph[n_id]).heuristic = euclidean_distance(self.graph[self.end_id], self.graph[n_id])
        elif h == 'Manhattan':
            for n_id in self.graph:
                (self.graph[n_id]).heuristic = manhattan_distance(self.graph[self.end_id], self.graph[n_id])       
        else:
            print('\n Not implemented yet \n')
            
    def run_astar(self):

        if self.start_id not in self.graph:
            print('\n Start-point does not exist \n')
            return

        ############
        #the length of both list is max of number of vertices
        #each element will not have the same length
        iter_visited_x = []
        iter_visited_y = []
        iter_queued_x = []
        iter_queued_y = []
        ############

        #frontier works in tandem with pq
        explored = set()
        frontier = {}

        #initialize pq and frontier
        pq = pqClass.PriorityQueue(name = 'PQ_ASTAR')
        #calculate f(n) = g(n) + h(n)
        f_n = self.graph[self.start_id].cum_weights + self.graph[self.start_id].heuristic
        pq.insert(self.start_id, f_n)
        frontier[self.start_id] = f_n
        (self.graph[self.start_id]).cum_weights = 0

        #corner case
        if self.start_id == self.end_id:
            print('\n Start == End \n')
 
        while not pq.is_empty():
            
            #print("Current queue : ", pq.queue)
            v = pq.remove() 
            frontier.pop(v)
            #print("Current vertex : ", v)

            if v not in explored:

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

                neighbours = (self.graph[v]).neighbors
                weights = (self.graph[v]).weights
                #print(neighbours, weights)
                
                for n, w in zip(neighbours, weights):

                    #check feasibility of movements
                    if n not in self.graph:
                        continue

                    if n not in explored:

                        #check if n is in frontier, with any w (no duplicate in frontier)
                        if n not in frontier:
                            #if not in frontier, add to the pq and frontier
                            #using the cumulative cost of edges + heuristic!
                            cum_w = (self.graph[v]).cum_weights + w
                            (self.graph[n]).parent_id = v
                            (self.graph[n]).cum_weights = cum_w

                            #calculate f(n) = g(n) + h(n)
                            f_n = cum_w + self.graph[n].heuristic

                            pq.insert(n, f_n)
                            frontier[n] = f_n
                        else:
                            #if is in frontier, check the path f(n) in the frontier
                            f_n_old = frontier[n]
                            #calculate the new f(n)
                            cum_w = (self.graph[v]).cum_weights + w
                            f_n = cum_w + self.graph[n].heuristic

                            #if prev. cost is higher, replace in frontier and pq
                            if f_n_old > f_n:
                                frontier[n] = f_n
                                (self.graph[n]).parent_id = v
                                #replace the said element in pq
                                pq.replace(n, f_n)
                                (self.graph[n]).cum_weights = cum_w
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
                for e in frontier:
                    temp_x.append((self.graph[e]).x)
                    temp_y.append((self.graph[e]).y)
                iter_queued_x.append(temp_x)
                iter_queued_y.append(temp_y)
                ############

        return self.found_flag