import sys
T=int(sys.stdin.readline())
sum=0
for _ in range(T):
    n=int(sys.stdin.readline())
    stock=list(map(int,sys.stdin.readline().split()))
    sum=0
    maxs=stock[-1]    # 현재 최대값 설정
    for i in range(len(stock)-2,-1,-1):   # 리스트 거꾸로 for문 돌리기
        if maxs-stock[i]>=0:   #최대값과 stock 값 비교
            sum+=maxs-stock[i]
        else:
            maxs=stock[i]
    print(sum)                
            



