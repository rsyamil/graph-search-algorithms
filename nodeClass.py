

class Node:
    def __init__(self, x=0, y=0, z=0, act=[]):
        self.x = x
        self.y = y
        self.z = z
        self.action = act
        self.neighbors = []
        self.weights = []
        self.cum_weights = 0
        self.id = str(x)+'-'+str(y)+'-'+str(z)
        self.parent_id = '-999'

    def get_data(self):
        print('Coordinates of {}:\t ({}, {}, {})'.format(self.id, self.x, self.y, self.z))
        print('Possible actions :\t{}'.format(self.action))



