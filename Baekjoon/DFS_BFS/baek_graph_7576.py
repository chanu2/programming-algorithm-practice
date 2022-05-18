# import sys
# from collections import deque
# sys.setrecursionlimit(10**5)         # 재귀함수 제한
# dx=[1,-1,0,0]            # 동서남북 확인
# dy=[0,0,1,-1]   

# def bfs(queue):           
#     global cnt           # 글로벌 변수 선언
#     a=deque([])  
#     cnt+=1
#     while queue:                               ######## 메모리초과 #######
#         x,y=queue.popleft()
#         for i in range(4):
#             xx=x+dx[i]
#             yy=y+dy[i]
#             if 0<= xx <n and 0<= yy <m:
#                 if graph[xx][yy]==0:
#                     graph[xx][yy]=1
#                     a.append([xx,yy])    # 새로운 리스트에 변수를 추가한다.

#     queue=a      # queue에 a를 넣어준다. 
#     if queue :   # 
#         bfs(queue)
              
   
                    
# m,n=map(int,sys.stdin.readline().split())
# graph=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
# cnt=-1      # 처음 시작할 때는 하루가 지나지 않은 상태이기 때문에
# queue=deque([])         
# for i in range(n):         # 모든 리스트를 탐색하여 1이 있는 위치를 큐에 추가한다.
#     for j in range(m):
#         if graph[i][j]==1:
#             queue.append([i,j])  
# bfs(queue) 
# for i in range(n):
#     for j in range(m):
#         if graph[i][j]==0:   
#             print(-1)
#             exit()
# print(cnt)




#### 재귀함수를 사용하지 않는 코드 ####
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def tomato(queue):
    global cnt     # 글로벌 변수를 선언한다

    while queue:
        cnt+=1
        
        for _ in range(len(queue)):   # 큐 안에 존재하는 요소의 수를 반복해준다.  !!! 핵심 코드 !!!
            x,y=queue.popleft()       # 
            
            
            for j in range(4):    # 동서남북을 확인
                xx=x+dx[j]
                yy=y+dy[j]
                if 0<= xx <n and 0<= yy <m:   
                    if graph[xx][yy]==0:
                        graph[xx][yy]=1
                        queue.append([xx,yy])   # 큐안에 추가 하지만 for문에는 영향을 주지 않는다.
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                return -1

    return cnt                 

 

m,n=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
cnt=-1   # 첫날에는 토마토가 익지 않기 때문에 
queue=deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])   
print(tomato(queue))            


    


