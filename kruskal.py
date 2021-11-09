def find(parent, i):
    if parent[i] == i: return i
    return find(parent, parent[i])

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y: parent[x] = y
    else: parent[y] = x

def kruskal(graph, V):
    graph = sorted(graph, key=lambda x: x[2])

    #init parent
    parent = []
    for node in range(V):
        parent.append(node)
    
    result = [] 

    cntEdge = 0 #number of connecting edge
    idx = 0 #graph index

    while cntEdge < V - 1: #until all edges are connected
        u, v, w = graph[idx]
        idx += 1

        x = find(parent, x)
        y = find(parent, y)

        if x != y: #The edge is not make cycle
            cntEdge += 1
            union(parent, x, y)
    
    minCost = 0
    for u, v, w in result:
        minCost += w
        print("%d --- %d" % (u, v))
    print("minimum cost is ", minCost)
