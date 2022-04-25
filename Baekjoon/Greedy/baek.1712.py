import math                  
a,b,c=map(int,input().split())
if b>=c:
    print(-1)
elif b<c: 
    bep=a/(c-b)+1       #손익분기점 계산
    print(math.trunc(bep)) # 소수점 자리 모두 제거
        