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
        self.bfs_trasversal_output =[]
        self.adj_list = {}
        self.queue = Queue()
        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)
        self.path = []

    def findPath(self):
        c = 0
        self.visited[self.source] = 1
        self.level[self.source] = 0
        self.queue.put(self.source)

        self.adj_list = self.grid.getAdjacentNodes()

        print("Adj list", self.adj_list)


        # while not self.queue.empty():
        #     u = self.queue.get()
        #     self.bfs_trasversal_output.append(u)

        #     for node in self.adj_list[u]:
        #         if not self.visited[node]:
        #             self.visited[node]  = 1
        #             self.parent[node] = u
        #             self.level[node] = self.level[u] + 1
        #             self.queue.put(node)

        # while self.target is not None:
        #     self.path.append(self.target)
        #     self.target = self.parent[self.target]
        
        # reversed_path = self.path.reverse

        # for p in range(reversed_path):
        #     reversed_path[p] = 1

        # return reversed_path
        return []


class DepthFirstSearch:
    def __init__(self, source, target, grid_env) -> None:
        self.source  = source
        self.target = target
        self.grid_env = grid_env


class Dijkstra:
    def __init__(self, source, target, grid_env) -> None:
        self.source  = source
        self.target = target
        self.grid_env = grid_env




        