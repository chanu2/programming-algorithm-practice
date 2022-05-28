import sys
k=int(sys.stdin.readline().rstrip())
data=[]
for _ in range(k):
    num=int(sys.stdin.readline().rstrip())
    if num!=0:
        data.append(num)
    else:
        data.pop()
print(sum(data))            
