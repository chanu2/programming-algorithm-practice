import sys
rectangle=[]     
square=[]
n,m=map(int,sys.stdin.readline().split())
for _ in range(n):
    rectangle.append(list(map(int,sys.stdin.readline().rstrip())))
     
for i in range(n):
    for j in range(m):                # out of range 주의!
        for k in range(j+1,m):
            if rectangle[i][j]==rectangle[i][k] and (k-j)<=(n-1)-i :  # l이 범위가 out of range하지 않도록 하는 코드
                l=k-j
                if rectangle[i][k]==rectangle[i+l][k]==rectangle[i+l][k-l]: 
                    square.append((l+1)**2)  #정사각형 넓이 구하는 코드

if len(square)==0:
     print(1)

else:
    print(max(square))  # 최대값을 출력
                    