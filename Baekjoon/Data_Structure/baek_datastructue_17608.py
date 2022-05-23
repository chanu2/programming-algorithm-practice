import sys
n=int(sys.stdin.readline().rstrip())
stick=[int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt=1
right=stick.pop()
for _ in range(len(stick)):
    current=stick.pop()
    if right<current:
        right=current
        cnt+=1
        
print(cnt)        
