import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data, create empty lists for visited, queue, and path, 
        and create empty dictionary for storing parent nodes
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
        self.visited = []
        self.queue = []
        self.backtrace = {} # keep track of parent nodes
        self.path = [] # shortest path

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        # add start node to queue 
        self.queue.append(start)

        # mark start node as visited
        self.visited.append(start)

        if start==end:
            return self.visited

        # while there is a queue, dequeue current node and loop through unvisited neighbors of current node
        while self.queue:
            just_popped = self.queue.pop(0) # first in first out
            for neighbor in self.graph.neighbors(just_popped):
                if neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.append(neighbor)
                    self.backtrace[neighbor]=just_popped # set pointer from neighbor to current (parent) node 
                    
                    # If there is an end node and a path exists, return a list of the shortest path
                    if neighbor==end:
                        curr_node = end
                        self.path.append(curr_node)
                        while curr_node!=start:
                            parent = backtrace[curr_node] # identify parent node
                            self.path.append(parent) # add parent node to path
                            curr_node = parent # set current node to parent node
                        path.reverse() # reverse direction of path
                        return path 
        
        # If there's no end node, just return a list with the order of traversal
        if end==None:
            return self.visited
        
        # If there is an end node and a path does not exist, return None
        if end not in self.visited:
            return None