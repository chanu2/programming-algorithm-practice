import sys 
n,a,b=map(int,sys.stdin.readline().split())  
cnt=0
while a!=b:
    a-=a//2    # 현재 위치를 구하는 코드
    b-=b//2   
    cnt+=1    
print(cnt)    
    


