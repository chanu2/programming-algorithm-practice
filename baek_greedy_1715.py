import sys
import heapq     #우선순위 큐 -> 완전 이진트리
n=int(sys.stdin.readline())
number=[int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(number)  #오름차순 정렬 (logn)
sum=0
result=0

    
for _ in range(len(number)-1):
    a=heapq.heappop(number)   # 가장 최소값을 pop한다
    b=heapq.heappop(number) 
    sum=a+b
    result+=sum
    heapq.heappush(number,sum)  # 자동으로 순서에 맞추어 push된다
print(result)