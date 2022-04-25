n=int(input())
i=1
cnt=0
while n>=0:
    n-=i
    i+=1
    cnt+=1
    if n<0:
        print(cnt-1)    

