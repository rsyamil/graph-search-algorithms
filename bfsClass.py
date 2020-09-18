from collections import deque

class BFS:
    def __init__(self, name=[], graph=0, start_id=0, end_id=0):
        self.name = name
        self.graph = graph
        self.start_id = start_id
        self.end_id = end_id
        self.found_flag = False

    def run_bfs(self):
        explored = set()
        queue = deque([self.start_id])

        #corner case
        if self.start_id == self.end_id:
            print('\n Start == End \n')
        
        while queue:
            
            #print("Current queue : ", queue)
            v = queue.popleft()
            #print("Current vertex : ", v)
            
            if v not in explored:
                neighbours = (self.graph[v]).neighbors
                #print(neighbours)
                
                for n in neighbours:
                    if n not in explored:
                        (self.graph[n]).parent_id = v
                        queue.append(n)
                
                explored.add(v)

                if (v == self.end_id):
                    print('\n Found \n')
                    self.found_flag = True
                    return self.found_flag
        return self.found_flag
    
