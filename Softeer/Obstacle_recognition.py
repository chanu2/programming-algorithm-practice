import sys
def block(x,y):
    global cnt;

    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        cnt+=1
        block(x-1,y)
        block(x+1,y)
        block(x,y-1)
        block(x,y+1)
        
        return True
    return False

n=int(sys.stdin.readline())
graph=[ list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
result=0
answer=[]
for i in range(n):
    for j in range(n):
        cnt=0
        if block(i,j)==True:
            answer.append(cnt)
            result+=1
answer.sort()
print(result)
[print(i) for i in answer]            
           
   