def printParent(node, adj, parent):
    if parent == 0:
        print(node, " -> Root")
    else:
        print(node, " -> ", parent)

    for i in adj[node]:
        if i != parent:
            printParent(i, adj, node)


adj = []
n = 7
root = 1
for i in range(0, n+1):
    adj.append([])

adj[1].append(2)
adj[1].append(3)
adj[1].append(4)

adj[2].append(1)
adj[2].append(5)
adj[2].append(6)

adj[3].append(1)

adj[4].append(1)
adj[4].append(7)

adj[5].append(2)
adj[6].append(2)

adj[7].append(4)
print(adj)

printParent(root, adj, 0)
