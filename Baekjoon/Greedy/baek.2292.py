
n=int(input())
i=1
sum=1
while True:
    if n==1:
        print(1) # n이 1이면 1을 출력
        break
    sum+=6*i     # 등비가 6인 수열 
    if sum>=n: 
        print(i+1)
        break
    i+=1



