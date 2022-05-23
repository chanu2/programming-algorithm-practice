import sys
from collections import deque   # 큐 선언
dx=[1,-1,0,0]    
dy=[0,0,1,-1]

def bfs(x,y,color,graph):  
    queue=deque([])
    queue.append([x,y])
    visited[x][y]=1   # 방문처리

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<= xx< n and 0<= yy< n: 
                if graph[xx][yy]==color:
                    if visited[xx][yy]==0:   # 방문한 곳이 아니라면 
                        visited[xx][yy]=1    # 그곳을 방문처리
                        queue.append([xx,yy])

n=int(sys.stdin.readline().rstrip())
graph=[(sys.stdin.readline().strip())for i in range(n)]  # 적록색맹이 아닐때 
visited=[[0]*n for i in range(n)]  # 방문처리할 곳
graph2=[[0]*n for i in range(n)]   # 적록색맹일 때 
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R'or graph[i][j]=='G':    # 적록색맹일 때 G 와 R을 구분하지 못하기 때문에 
            graph2[i][j]=3       # 어떠한 수로 저장
        else:
            graph2[i][j]=2   

            


result=0
disable_color=0

for i in range(n):
    for j in range(n):
        if graph[i][j]== 'R' or graph[i][j]== 'G' or graph[i][j]== 'B':   # 그래프를 확인 하면서 R,G,B가 나왔을 때
            
            if visited[i][j]==0:
                
                bfs(i,j,graph[i][j],graph)    # 그때 의 색과 적록색맹이 아닐 때 그래프를 넣어준다
                result+=1



              

visited=[[0]*n for i in range(n)]       # 방문처리 할 곳을 초기화

for i in range(n):
    for j in range(n):
        if graph2[i][j]==2 or graph2[i][j]==3:
            if visited[i][j]==0:
                bfs(i,j,graph2[i][j],graph2)     
                disable_color+=1
                

print(result,disable_color)                



