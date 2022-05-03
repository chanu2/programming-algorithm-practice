import sys
from collections import deque
dx=[1,-1,0,0]      
dy=[0,0,1,-1]      # 상하 좌우 확인 

def bfs(x,y):
    global cnt  # 글로벌 변수로 선언
    queue=deque([])
    queue.append([x,y])
    graph[x][y]=0  # 처음 방문한 곳 방문 처리
    cnt=1   # 처음 방문한 곳 1 카운트
    

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<= xx <n and 0<= yy <n:  # 제한 조건
                if graph[xx][yy]==1:
                    graph[xx][yy]=0 # 방문처리
                    queue.append([xx,yy])
                    cnt+=1   # 방문 처리 후 카운트
                    
                    

n=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().strip()))  for _ in range(n)]
result=0  # 구역의 수
answer=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)   
            result+=1  # 구역의 수 카운트
            answer.append(cnt) # 구역 안의 개수를 리스트에 추가
            cnt=0  # 하나의 구역을 모두 탐색 후 카운 트 초기화
answer.sort()  #구역안에 개수를 오름차순 정렬
print(result)
[print(k) for k in answer]            


