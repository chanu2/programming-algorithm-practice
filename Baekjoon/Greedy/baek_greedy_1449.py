import sys
cnt=1
n,m=map(int,sys.stdin.readline().split())
plumbing=list(map(int,input().split()))
plumbing.sort()      # 오름차순으로 정리 한다(핵심)
start=plumbing[0]
end=plumbing[0]+m
for i in range(n):
    if start<=plumbing[i]<end:        # 구간 안에 존재할때 사용하는 코드! 
        pass
    else:                           
        cnt+=1                        # else에 걸릴떄 cnt에 1을 더해준다
        start=plumbing[i]             # start 와 end 값을 변경해준다.
        end=plumbing[i]+m
        
print(cnt)            



    




