import heapq

class PriorityQueue:

    def __init__(self, name=[]):
        self.name = name
        self.queue = []

    def insert(self, vertex, priority):
        heapq.heappush(self.queue, (priority, vertex))

    def remove(self):
        priority, vertex = heapq.heappop(self.queue)
        return vertex

    def is_empty(self):
        return len(self.queue) == 0

    #function to replace and heapify
    def replace(self, vertex, priority):

        #print('THIS HAPPENED')

        for t_idx, t in enumerate(self.queue):
            if vertex == t[-1]:
                #print('THIS HAPPENED TOO??')
                self.queue[t_idx] = (priority, vertex)
                break
        heapq.heapify(self.queue)

