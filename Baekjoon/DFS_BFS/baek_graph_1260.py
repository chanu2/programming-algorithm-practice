#DFS
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)  

#BFS
def bfs(graph,v,visited):
    visited[v]=True
    queue = deque([v])
    while queue:
        v1=queue.popleft()
        print(v1,end=' ')
        for i in graph[v1]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


from collections import deque
import sys
n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()

#함수 실행
dfs(graph,v,visited)
visited=[False]*(n+1)
print()        
bfs(graph,v,visited)