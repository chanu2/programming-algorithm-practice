import sys
r,c=map(int,sys.stdin.readline().split())
origin=[]
change=[]
cnt=0

for _ in range(r):
    origin.append(list(map(int, input()))) 
    
for _ in range(r):       
    change.append(list(map(int, input())))



for i in range(r-2):       #범위를 넘지 않도록 잡는다
    for j in range(c-2):     
        if origin[i][j]!=change[i][j]:    
            
            for k in range(i,i+3):
                for p in range(j,j+3):  #3 by 3 행렬 뒤집는 코드
                    origin[k][p]=1-origin[k][p]
            cnt+=1        

for i in range(r):     #두 행렬을 모두 비교!
    for j in range(c):
        if origin[i][j]!=change[i][j]: # 하나라도 다르다면 -1반환
            print(-1)           
            exit()
else:
    print(cnt)   # 모두 같다면 cnt값 반환
    



         



