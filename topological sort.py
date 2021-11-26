from collections import deque

V, E = map(int, input().split())

indegree = [0 for _ in range(V + 1)]
graph = {key: list() for key in range(V+1)}

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v) # u -> v
    indegree[v] += 1 
    
def topological_sort():
    q = deque()
    
    #indegree is 0
    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        #vertex = q.pop(0)
        vertex = q.popleft()
        print(vertex, end=" ") #sorted
        
        for i in graph[vertex]:
            indegree[i] -= 1
            #indegree is 0
            if indegree[i] == 0: q.append(i)
            
topological_sort()