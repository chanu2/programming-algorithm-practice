import sys
x,y,w,h=map(int,sys.stdin.readline().split())
result=[]
result.append(w-x)
result.append(x-0)
result.append(h-y)
result.append(y-0)
print(min(result))

