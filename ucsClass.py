import pqClass
import pickle

class UCS:
    def __init__(self, name=[], graph=0, start_id=0, end_id=0):
        self.name = name
        self.graph = graph
        self.start_id = start_id
        self.end_id = end_id
        self.found_flag = False

    def run_ucs(self):

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
        pq = pqClass.PriorityQueue(name = 'PQ_UCS')
        pq.insert(self.start_id, 0)
        frontier[self.start_id] = 0
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
                            #using the cumulative cost of edges
                            cum_w = (self.graph[v]).cum_weights + w
                            pq.insert(n, cum_w)
                            frontier[n] = cum_w
                            (self.graph[n]).parent_id = v
                            (self.graph[n]).cum_weights = cum_w
                        else:
                            #if is in frontier, check the path cum. cost in the frontier
                            cum_cost = frontier[n]
                            cum_w = (self.graph[v]).cum_weights + w
                            #if prev. cost is higher, replace in frontier and pq
                            if cum_cost > cum_w:
                                frontier[n] = cum_w
                                (self.graph[n]).parent_id = v
                                #replace the said element in pq
                                pq.replace(n, cum_w)
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