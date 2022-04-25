import sys
n=int(sys.stdin.readline())
level=[]
cnt=0
for _ in range(n):
    level.append(int(sys.stdin.readline()))

level.reverse() # 리스트 뒤집기

if len(level)==1:
    print(level[0])
    exit()
for i in range(len(level)-1):
    if level[i]<=level[i+1]:
        cnt+=level[i+1]-level[i]+1
        level[i+1]=level[i]-1

print(cnt)         


        

