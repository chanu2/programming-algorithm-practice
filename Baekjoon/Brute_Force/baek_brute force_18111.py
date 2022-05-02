import sys
n,m,b=map(int,sys.stdin.readline().split())
block=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
mini=sys.maxsize #int의 최댓값을 확인 
hight=0
for i in range(257): #최대 256까지의 경우의수
    cntapp=0     # 블록을 1개 추가할때 걸리는 시간
    cntsub=0     # 블록을 1개 제거하고 인벤토리에 추가하는 시간
    for j in range(n):  
        for k in range(m):
          
            if block[j][k]>i:
                cntsub+=(block[j][k]-i)   # i 보다 클때
            else:
                cntapp+=(i-block[j][k])    # i보다 작을 때
    
    if b+cntsub<cntapp:    # 추가할 수 있는 블록의 수와 제거한 블록의 수의 성립조건
        continue           # 성립한다면 최상단 for문으로 이동 
    t=cntapp+cntsub*2
    if mini>=t:     # 최소값을 구하는코드
        mini=t
        hight=i     # 최소일때 높이값
print(mini,hight)