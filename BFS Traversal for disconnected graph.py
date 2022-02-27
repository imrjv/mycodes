from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def bfsTraversal(self):
        visited = [False] * (max(self.graph) + 1)
        for s in range(1, len(visited)):
            if visited[s] is not True:
                queue = []
                queue.append(s)
                visited[s] = True
                while len(queue) != 0:
                    s = queue.pop(0)
                    print(s, end=' ')
                    for i in self.graph[s]:
                        if visited[i] == False:
                            queue.append(i)
                            visited[i] = True


g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 7)
g.addEdge(3, 5)
g.addEdge(3, 2)
g.addEdge(5, 3)
g.addEdge(5, 7)
g.addEdge(7, 2)
g.addEdge(7, 5)
g.addEdge(4, 6)
g.addEdge(6, 4)

g.bfsTraversal()

''' 

    1 ----- 2 ----- 3         4 ----- 6
            |       |
            |       |
            7 ----- 5    
    *Disconnected Graph
    
 Output -> 1 2 3 7 5 4 6
 
 '''
