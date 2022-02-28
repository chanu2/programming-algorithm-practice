sum=0
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(n):
    sum+=min(A)*max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(sum)

    

