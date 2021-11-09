import sys
def minKey(key, mstSet, V):
    mini = sys.maxsize
    for v in range(V):
        if key[v] < mini and mstSet[v] == False:
            mini = key[v]
            min_idx = v
    return min_idx

def prim(graph, V):
    key = [sys.maxsize] * V
    parent = [None] * V

    key[0] = 0 #it's picked as first vertex    
    mstSet = [False] * V

    for cout in range(V):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = grap[u][v]
                parent[v] = u
    print(parent)