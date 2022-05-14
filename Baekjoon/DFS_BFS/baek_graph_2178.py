import sys
from collections import deque

def maze_bsf(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1] 

    queue=deque([])
    queue.append([x,y])
    
    

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]

            if 0<= xx <n and 0<= yy <m:
                if graph[xx][yy]==1:
                    graph[xx][yy]=graph[x][y]+1    # 방문처리해주면서 도착한 graph[xx][yy]를 기준으로 상하좌우 어디를 가든 graph[x][y]+1값으로 고정해주면 지나온 거리를 확인 할 수 있다. 
                    queue.append([xx,yy])
    return graph[n-1][m-1]      # 마지막 위치를 반환해준다            

n,m=map(int,sys.stdin.readline().split())
graph=[ list(map(int,sys.stdin.readline().strip()))for _ in range(n)]

print(maze_bsf(0,0))