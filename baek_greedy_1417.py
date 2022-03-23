import sys
vote=[]
count=0
n=int(sys.stdin.readline())
for _ in range(n):
    vote.append(int(sys.stdin.readline()))
congressman1=vote.pop(0)    
if n==1:
    print(0)
else:
    while True:
        if congressman1>max(vote):
            print(count)
            break
        elif congressman1<=max(vote):
            a=vote.index(max(vote))        # 가장큰수를 찾는다
            vote[a]-=1
            congressman1+=1
            count+=1

        
        

    
    