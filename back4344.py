n=int(input())

for _ in range(n):
    data=list(map(int,input().split()))
    sum=0
    count=0
    
    for j in data[1::]:
        sum+=j
    average=(sum/data[0])
    for k in data[1::]:
        if k>average:
            count+=1
    a=(count/data[0]*100)
    print("{:.3f}%".format(a))  # 40.000을 만들기 위해서 소수점 3번째 부분을 없애지 않고 0으로 채우는 코드
    

    

        