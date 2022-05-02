# import sys                  # DFS를 이용하여 문제를 풀었지만 런타임 에러 발생

# def find_cabbage(x,y):
#     if x<=-1 or x>=N or y<=-1 or y>=N:   # 범위를 설정해주는 코드
#         return False
#     if field[x][y]==1:
#         field[x][y]=0
#         find_cabbage(x-1,y)     # 재귀함수를 이용한 dfs
#         find_cabbage(x,y-1)
#         find_cabbage(x+1,y)
#         find_cabbage(x,y+1)

#         return True
#     return False


# T=int(sys.stdin.readline())
# for _ in range(T):
#     cnt=0
#     M,N,K=map(int,sys.stdin.readline().split())
#     field=[[0]*M for _ in range(N)]
    
#     for _ in range(K):
#         x,y=map(int,sys.stdin.readline().split())
#         field[x].insert(y,1)

#     for i in range(N):
#         for j in range(M):
#             if find_cabbage(i,j)==True:
#                 cnt+=1
#     print(cnt)            


# # BFS로

import sys
from collections import deque    # 큐선언
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    queue=deque([])    # 큐를 생성한다
    queue.append([y,x]) 

    while queue: # 큐가 없을 때 까지 반복
        y,x=queue.pop() # 확인 후 데이터를 꺼낸다.
        for i in range(4):  #상하좌우를 확인한다.
            yy=y+dy[i]    
            xx=x+dx[i]
            if 0<=xx<M and 0<=yy<N:  # 제한조건
                if field[yy][xx]==1: 
                    field[yy][xx]=0
                    queue.append([yy,xx])  #데이터를 추가해준다



T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    cnt=0
    M,N,K=map(int,sys.stdin.readline().split())
    field=[[0]*M for _ in range(N)]
    
    for _ in range(K):
        x,y=map(int,sys.stdin.readline().split())   # 그래프 만들기
        field[y][x]=1
       

    for i in range(N):
        for j in range(M):
            if field[i][j]==1:     
                bfs(i,j)     # 함수를 탈출하면 카운트한다
                cnt+=1
    print(cnt)          
    
     




