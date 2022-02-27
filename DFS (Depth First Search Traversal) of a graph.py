from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def dfsTraversal(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsTraversal(i, visited)

    def dfs(self, v):
        visited = [False] * (max(self.graph) + 1)
        self.dfsTraversal(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)

'''
Output -> Following is DFS from (starting from vertex 2)
          2 0 1 3
          
'''
