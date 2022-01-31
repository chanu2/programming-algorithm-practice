n=int(input())               # ※ (9,9,9,9,9)  ->  등차수열!!
def sequence(n):             # 한수를 찾는 함수
    sum=0
    for i in range(1,n+1):
        i=str(i)
        if len(i)==1 or len(i)==2:    # 한자리수 and 두자리수는 모두 한수
            sum+=1
            
        elif len(i)==3:
            if int(i[2])-int(i[1])==int(i[1])-int(i[0]):   #각 자리수의 비교를 통해서 등차수열을 확인한 후 한수 찾는 코드
                sum+=1
    return sum
print(sequence(n))

