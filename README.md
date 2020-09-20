# graph-search-algorithms

This is my (rather efficient) implementation of graph search algorithms in Python. The implemented algorithms are Breadth-First Search (BFS), Depth-First Search (DFS), Uniform-Cost Search (UCS) and A* search. Pseudocodes are based on AIMA (Norvig and Russell, 3rd edition). The following figures can be re-produced from [this Jupyter Notebook](https://github.com/rsyamil/graph-search-algorithms/blob/master/display.ipynb) and the *input.txt* has the sample graph on a 2D plane. Note that the implementation works for 3D too but I have generated a simple 2D example for illustration purposes. 

## Un-Informed search algorithms (DFS and BFS)

GIF for **Depth-First Search (DFS)** as it progresses through the 2D space. Red-circles represent the final path found by the algorithm. Light-gray filled circles represents all traversable points in the 2D space. Teal-colored points are the explored nodes and yellow points are the expanded nodes (i.e. nodes that are added to the queue/stack/priorityqueue). Teal-colored square is the starting point and yellow square represents the end point. 

![DFS](/readme/DFS.gif)

GIF for **Breadth-First Search (BFS)** as it progresses through the 2D space. In both BFS and DFS, the weight of the edges is not taken into consideration and the nodes that are expanded depends on whether you use a FIFO or LIFO data structure.  
  
![BFS](/readme/BFS.gif)

## Informed search algorithms (UCS and A*)

One of the reasons why I created these GIFs is to convince myself that the implementation of these algorithms is correct and it is more easily verified with visuals. In **Uniform-Cost Search**, the algorithm considers the weight/cost of the edges connecting the nodes. So as UCS expands the nodes to be traversed, it will consider a uniform cumulative cost and will visit the nodes according to the cumulative cost to get to those nodes. This is the reason why the teal-colored points form a nice circular contour as UCS progresses through the 2D space. 

![UCS](/readme/UCS.gif)

GIF for **A* Search** as it progresses through the 2D space. In A* search, we consider a heuristic (that ideally should be admissible and consistent) such as Euclidean or Manhattan distances. The heuristic cost is added to the cumulative cost to get to the nodes to inform A* of the next best node to expand. The result of this is the nice distorted contour that leans towards the solution. Note that not all nodes are visited/expanded/added to the queue.

![ASTAR](/readme/ASTAR.gif)

The choice of data structures matters and in this implementation, I have utilized a heap for operations that require sorting and I keep a dictionary that works in tandem with the heap so elements within the heap can be accessed in constant time. 
