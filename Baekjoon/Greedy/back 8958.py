n=int(input())
for i in range(n):
    data=list(map(str,input()))
    origin=1
    sum=0
    for j in data:             #리스트 자체를 반복문으로 사용 
        if j=='o':
            sum+=origin         
            origin+=1
        else:
            origin=1
    print(sum)   
    

            



   