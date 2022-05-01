import sys
while True:
    P=list(map(int,sys.stdin.readline().split()))
    if sum(P)==0:
        break
    if P[0]**2==P[1]**2 + P[2]**2 or P[1]**2==P[0]**2 + P[2]**2 or P[2]**2==P[1]**2 + P[0]**2:
        print('right')   #피타고라스의 정리 원리
    else:
        print('wrong')    