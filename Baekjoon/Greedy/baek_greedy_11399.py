n=int(input())
sum=0
personal_time=list(map(int, input().split()))  
personal_time.sort()   # 오름차순으로 정렬한다.  //(최소 소요시간을 구하기 위해)
for i in range(n):
    for j in range(i+1):   # 이중 반복문을 통해서 개인의 소요시간을 구하는 코드
        sum+=personal_time[j]   # 개인의 소요시간을 모두 합하는 코드
print(sum)
