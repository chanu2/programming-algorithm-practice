import sys
n=int(sys.stdin.readline())
ball=sys.stdin.readline().rstrip()   
cnt=0
result=[]

a = ball.rstrip('R')    # R을 오른쪽으로 옮기는 
result.append(a.count('R'))

b = ball.rstrip('B')    # B을 오른쪽으로 
result.append(b.count('B'))

c = ball.lstrip('R')    # R을 왼쪽으로 
result.append(c.count('R'))

d = ball.lstrip('B')    # B을 왼쪽으로 
result.append(d.count('B'))

print(max(result))