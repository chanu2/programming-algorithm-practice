n=int(input())
sum=0
data=list(map(int,input().split()))     #여러개 입력 list로 입력받기

max=0
for i in range(1,n):
    if data[max]<data[i]:               # 최대값을 구현
        max=i
for k in range(n):
    sum+=data[k]                        # 원하는 평균 출력
print((sum/data[max]*100)/n)
               

