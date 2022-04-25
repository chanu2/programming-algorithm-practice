sum=0
n=int(input())
A=list(map(int,input().split()))   # 리스트로 여러개의 정수를 받는다
B=list(map(int,input().split())) 
for i in range(n):
    sum+=min(A)*max(B)         #각 리스트의 최소값과 최대값을 구한다 
    A.pop(A.index(min(A)))     # pop()를 사용하여 최소값이 있는 인덱스를 제거한다
    B.pop(B.index(max(B)))     # pop()를 사용하여 최대값이 있는 인덱스를 제거한다
print(sum)

    

