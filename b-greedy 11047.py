import math                             #수학 함수 선언
n,k=map(int,input().split())         
kind=[]
b=[]
sum=0

for i in range(n):
    kind.append(int(input()))          # 동전의 종류를 리스트에 삽입

while k!=0:
    mini=0
    
    for j in range(n):
        b.append(math.floor(k/kind[j]))    # k 값을 각각 동전을 나누어 소수점 자리를 내림하여 
                                           # 그 값을 새로운 리스트에 삽입
       
    for l in range(1,n):
        if b[l]>0:                         # 새로운 리스트에 0보다 큰 수 중 최소값을 구하는 코드
            if b[mini]>b[l]:
                mini=l
               
    k=k-(b[mini]*kind[mini])               # k에 (동전 종류* 최소값)을 빼주는 코드
    sum+=b[mini]                           # 총 사용한 동전의 개수
    b.clear()
print(sum)


        

