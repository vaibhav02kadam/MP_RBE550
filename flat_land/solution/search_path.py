from collections import deque
import math
from queue import Queue, PriorityQueue
from obstacle_field_env import*


class BreadthFirstSearch:
    """ 
        Breadth First Search class plans path based on BFS search algorithm
    """
    def __init__(self, source, target, grid) -> None:
        self.source  = source
        self.target = target
        self.grid = grid
        self.grid_env = grid.grid_env
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.bfs_trasversal_output =[]
        self.adj_list = {}
        self.queue = Queue()
        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)
        self.path = []

    def findPath(self):
        """ Key function for searching path in planner
        """
    
        self.adj_list = self.grid.getAdjacentNodes()

        for node in self.adj_list.keys():
            self.visited[node] = False
            self.parent[node] = None
            self.level[node] = -1

        self.visited[self.source] = True
        self.level[self.source] = 0
        self.queue.put(self.source)


        while not self.queue.empty():
            u = self.queue.get()
            
            self.bfs_trasversal_output.append(u)

            for node_ in self.adj_list[u]:

                if not self.visited[node_]:
                    self.visited[node_]  = 1
                    self.parent[node_] = u
                    self.level[node_] = self.level[u] + 1
                    self.queue.put(node_)
    
        while self.target is not None:
            self.path.append(self.target)
            self.target = self.parent[self.target]
        
        self.path.reverse()

        #DEBUG print("Path got",self.path)
        if len(self.path) != 0:
            self.path.pop(0)
            self.path.pop(len(self.path)-1)

        return self.path
        


class DepthFirstSearch:
    """ 
        Depth First Search class plans path based on DFS search algorithm
    """
    def __init__(self, source, target, grid) -> None:
        self.source  = source
        self.target = target
        self.grid= grid    
        self.visited = {}
        self.parent = {}
        self.grid_env = self.grid.grid_env
        self.deq = deque()
        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)
        self.path = []
        self.trav_path = []

    def findPath(self):
        """ Key function for searching path in planner
        """
        self.adj_list = self.grid.getAdjacentNodes()

        for node in self.adj_list.keys():
            self.visited[node] = False
            self.parent[node] = None

        node = self.source
        self.visited[self.source] = True
        self.trav_path.append(self.source)
        self.deq.append(self.source)

        while len(self.deq):

            u = self.deq.pop()

            for node_ in self.adj_list[u]:

                if node_ == self.target:
                    self.visited[node_]  = 1
                    self.parent[node_] = u
                    self.trav_path.append(node_)
                    self.deq.clear()
                    break
                
                if not self.visited[node_]:
                    self.visited[node_]  = 1
                    self.parent[node_] = u
                    self.trav_path.append(node_)
                    self.deq.append(node_)

        while self.target is not None:
            self.path.append(self.target)
            self.target = self.parent[self.target]
        
        self.path.pop()
        self.path.reverse()
        
        return self.path    

class Dijkstra:
    """ 
        Dijkstra class plans shortest path based on Dijstra search algorithm considering weights.
    """
    def __init__(self, source, target, grid) -> None:
        self.source  = source
        self.target = target
        self.grid = grid
        self.grid_env = self.grid.grid_env
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.queue = PriorityQueue()
        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)
        self.path = []
        self.dijkstra_trasversal_output =[]
        self.cost ={}

    def findPath(self):
        """ Key function for searching path in planner
        """
        self.adj_list = self.grid.getAdjacentNodes()
        self.visited = set()
        self.cost = {self.source : 0}   #Set cost of source zero
        self.parent = {self.source: None} 
        self.queue.put((0,self.source)) #Set priority queue to source
        
        while self.queue:
            while not self.queue.empty():
                _, u = self.queue.get() # Lowest cost node

                if u not in self.visited: break
            else:
                break
            self.visited.add(u)
            if u == self.target:
                break

            for node_ in self.adj_list[u]:  
                if node_ in self.visited: continue

                old_cost = self.cost.get(node_, float('inf'))
                new_cost = self.cost[u] +  math.dist(u, node_)

                if new_cost < old_cost: 
                    self.queue.put((new_cost, node_))
                    self.cost[node_] = new_cost
                    self.parent[node_] = u

        if self.target not in self.parent:
            return None
        while self.target is not None:
            self.path.append(self.target)
            self.target = self.parent[self.target]
        
        self.path.reverse()

        #DEBUG print("Path got",self.path)
        if len(self.path) != 0:
            self.path.pop(0)
            self.path.pop(len(self.path)-1)

        return self.path


class RandomPlanner:
    def __init__(self, source, target, grid ) -> None:
        self.source  = source
        self.target = target

        self.grid = grid
        self.grid_env = grid.grid_env
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.trav_path =[]
        self.adj_list = {}
        self.queue = Queue()
        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)    
        self.path = []    

    def findPath(self):
        self.adj_list = self.grid.getAdjacentNodes()

        for node in self.adj_list.keys():
            self.visited[node] = False
            self.parent[node] = None
            self.level[node] = -1

        self.visited[self.source] = 1
        self.level[self.source] = 0
        self.queue.put(self.source)


        while not self.queue.empty():
            u = self.queue.get()
            
            self.trav_path.append(u)

            random.shuffle(self.adj_list[u])
            for node_ in self.adj_list[u]:



                if not self.visited[node_]:
                    self.visited[node_]  = 1
                    self.parent[node_] = u
                    self.level[node_] = self.level[u] + 1
                    self.queue.put(node_)


        while self.target is not None:
            self.path.append(self.target)
            self.target = self.parent[self.target]
        
        self.path.reverse()

        # print("Path got",self.path)
        if len(self.path) != 0:
            self.path.pop(0)
            # self.path.pop(len(self.path)-1)

        return self.path
        
