import math
from queue import Queue
import queue


class BreadthFirstSearch:
    def __init__(self, source, target, grid_env) -> None:
        self.source  = source
        self.target = target
        self.grid_env = grid_env
        self.visited = {}
        self.level = {}
        self.bfs_trasversal_output ={}
        self.adj_list = {}
        self.queue = Queue()
        self.rows = len(self.grid_env[0])
        self.cols = len(self.grid_env)
        self.path = []

        self.getAdjList()
        


    def getAdjList(self):

        for row in range(self.rows):
            for col in range(self.cols):
                self.adj_list[(row, col)] = [(row, col+1), (row+1, col)]


    def findPath(self):

        self.visited[self.source] = True
        self.level[self.source] = 0
        self.queue.put(self.source)

        while not self.queue.empty():
            u = queue.get()
            self.bfs_trasversal_output.append(u)

            for node in self.adj_list[u]:
                if not self.visited[node]:
                    self.visited[node]  = True
                    self.parent[node] = u
                    self.level[node] = self.level[u] + 1
                    self.queue.put(node)

        while self.target is not None:
            self.path.append(self.target)
            self.target = self.parent[self.target]
        
        reversed_path = self.path.reverse

        for p in range(reversed_path):
            reversed_path[p] = 1

        return reversed_path








        