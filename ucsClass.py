import pqClass

class UCS:
    def __init__(self, name=[], graph=0, start_id=0, end_id=0):
        self.name = name
        self.graph = graph
        self.start_id = start_id
        self.end_id = end_id
        self.found_flag = False

    def run_ucs(self):

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
                    self.found_flag = True
                    return self.found_flag

                neighbours = (self.graph[v]).neighbors
                weights = (self.graph[v]).weights
                #print(neighbours, weights)
                
                for n, w in zip(neighbours, weights):

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
        return self.found_flag