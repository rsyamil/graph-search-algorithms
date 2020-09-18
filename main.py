import parserClass
import nodeClass
import graphClass
import bfsClass
import ucsClass


if __name__ == '__main__':

    #parse input file
    parser = parserClass.Parser(name='Search_algorithms')
    alg, bbox_dim, start_id, end_id, nodes = parser.file_parser()
    
    #populate the neighbors (self.neighbors) for each node and build the graph
    graph = {}
    grapher = graphClass.Graph(name='Grapher')
    for n in nodes:
        ns, wts = grapher.update_neighbors(n)
        n.neighbors = ns
        n.weights = wts
        graph[n.id] = n
    #grapher.print_graph(graph)

    #call the algorithm on the graph
    if (alg == 'BFS'):
        print('\n Running BFS algorithm \n')
        bfs = bfsClass.BFS(name='BFS', graph=graph, start_id=start_id, end_id=end_id)
        found_flag = bfs.run_bfs()
        #grapher.print_graph_parents(graph)
        #backtrack and pass output to parser class
        output = grapher.backtrackBFS(graph, start_id, end_id, found_flag)
    elif (alg == 'UCS'):
        print('\n Running UCS algorithm \n')
        ucs = ucsClass.UCS(name='ucs', graph=graph, start_id=start_id, end_id=end_id)
        found_flag = ucs.run_ucs()
        #grapher.print_graph_parents(graph)
        output = grapher.backtrackUCS(graph, start_id, end_id, found_flag)
    else:
        print('\n Running A* algorithm \n')


    parser.file_writer(output, graph, found_flag)


            