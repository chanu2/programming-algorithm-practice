import sys
import heapq
heap = []
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    data=int(sys.stdin.readline())
    if data!=0:
        heapq.heappush(heap,(-data,data))  # 집합으로 heap에 넣을 수 있다.
    else:
        if not heap:
            print(0)
        else:
            a=heapq.heappop(heap)   # 꺼낼 때 -data기준으로 뽑을 수 있다
            print(a[1])    



