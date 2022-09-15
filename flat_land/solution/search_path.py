import math
from queue import Queue
import queue
from obstacle_field_env import*


class BreadthFirstSearch:
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
    
        self.adj_list = self.grid.getAdjacentNodes()

        for node in self.adj_list.keys():
            # print("Node in adajency", node)
            self.visited[node] = False
            self.parent[node] = None
            self.level[node] = -1

        self.visited[self.source] = True
        self.level[self.source] = 0
        self.queue.put(self.source)

        # print("Adjency list", self.adj_list)

        while not self.queue.empty():
            u = self.queue.get()
            
            self.bfs_trasversal_output.append(u)
            # print("adjeceny list of u",u, self.adj_list[u])

            for node_ in self.adj_list[u]:
                # print("U", u, node_)
                # print("Node  adj ", node_)

                if not self.visited[node_]:
                    self.visited[node_]  = 1
                    self.parent[node_] = u
                    self.level[node_] = self.level[u] + 1
                    self.queue.put(node_)
        
        # DEBUG print("BFS output ",self.bfs_trasversal_output)

        while self.target is not None:
            self.path.append(self.target)
            self.target = self.parent[self.target]
        
        self.path.reverse()

        print("Path got",self.path)
        if len(self.path) != 0:
            self.path.pop(0)
            self.path.pop(len(self.path)-1)

        return self.path
        


class DepthFirstSearch:
    def __init__(self, source, target, grid) -> None:
        self.source  = source
        self.target = target
        self.grid= grid
        self.color = {}  #White not visited at all,   #Grey vertex visited #Black Vertex and adjanecy explored 
        self.parent ={}
        self.traversal_time = {}
        self.dfs_traversal_output = []
        self.time = 0

    def findPath(self):

        self.adj_list = self.grid.getAdjacentNodes()

        for node in self.adj_list.keys():
            self.color[node] = "W"
            self.parent[node] = None
            self.traversal_time[node] = [-1, -1]


    def dfs_util(self, u):
        self.color[u] = "G"
        self.traversal_time[u][0] = self.time
        self.dfs_traversal_output.append(u)

        for v in self.adj_list[u]:
            if self.color[v] = "W":
                self.parent[v] = u
                self.dfs_util(v)




class Dijkstra:
    def __init__(self, source, target, grid_env) -> None:
        self.source  = source
        self.target = target
        self.grid_env = grid_env



class RandomPlanner:
    def __init__(self, source, target, grid_env) -> None:
        self.source  = source
        self.target = target
        self.grid_env = grid_env
        