import sys
n,m=map(int,sys.stdin.readline().split())   
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]    

for i in range(n):
    for j in range(n):
        if j!=0:  # 인덱스 0열인 곳은 더하지 않는다.
            graph[i][j]=graph[i][j]+graph[i][j-1]  # 끝 열까지 순차적으로 더해준다.
              #ex) [[1 ,2 ,3, 4]                  [[1,3,6,10]
              #     ,[2 ,3 ,4, 5]      ----->     ,[2,5,9,14] 
              #     ,[3, 4 ,5 ,6]      ----->     ,[3,7,12,18]
              #     ,[4 ,5, 6 ,7]]                ,[4,9,15,22]]
        
for k in range(m): 
    sum=0
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())  
    for p in range(x1-1,x2):   #  X1-1(인덱스 0부터 시작하기 떄문에) 축부터 X2 축의 x축만큼을 반복해준다
        if y1!=1:              # y축의 y1이 인덱스가 0으로 시작하지 않을때 
            sum-=graph[p][y1-2] # y축의 graph[p][y1-2]인 (y1-2)만크을 빼 주어야한다.
        sum+=graph[p][y2-1]   # 열이 y2까지 더한다 (인덱스가 0부터 시작하기 때문에 -1을 해줘야한다) 
    print(sum)     