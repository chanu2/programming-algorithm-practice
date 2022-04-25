import sys
n=int(sys.stdin.readline())
one=list(map(int,sys.stdin.readline().split()))
grow=list(map(int,sys.stdin.readline().split()))

result=sum(one)
grow.sort()
for i in range(1,n):      
    result+=grow[i]*(i)
print(result)    
    


# 리스트를 이중 리스트로 변환 후 lambda 함수를 사용해서 정렬하는 코드
# a=[]
# for i in range(n):
#     a.append([one[i],grow[i]])
# a = sorted(a, key = lambda x : x[1]) # key로 정렬하는 코드 key에는 항상 함수가 들어가야한다 ex)인자로 들어온 값에 2를 곱해서 반환한다고 하면 lambda x : x * 2 
# print(a)
  
