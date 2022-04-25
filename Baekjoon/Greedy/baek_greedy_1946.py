import sys
T=int(sys.stdin.readline())      
for _ in range(T):
    data=[]
    n=int(sys.stdin.readline())  #input() 내장 함수는 parameter로 prompt message를 받을 수 있다.
    for i in range(n):           #sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
        a,b=map(int,sys.stdin.readline().split())
        data.append([a,b])
    data.sort()    #오름차순으로 정렬
    max=data[0][1]
    cnt=1
    for j in range(1,n):
        if max>data[j][1]:    
            cnt+=1
            max=data[j][1]
    print(cnt)        


                


