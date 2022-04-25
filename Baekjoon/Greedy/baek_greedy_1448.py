import sys
length=[]
n=int(sys.stdin.readline())
for _ in range(n):
    length.append(int(sys.stdin.readline()))
length.sort(reverse=True)   # 내림차순 정렬
i=0
while i+3<=n:
    result=length[i:i+3]    # 리스트내부에 순서대로 3개를 슬라이싱하는 코드
    if result[0]<result[1]+result[2]:  #삼각형의 성립조건  가장긴변<나머지 변의 합
        print(sum(result))
        break
    i+=1
else:  # while문을 탈출하지 못하면 실행되는 코드
    print(-1)        

        



