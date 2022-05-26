import sys
import heapq
heap = []
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    data=int(sys.stdin.readline())
    if data!=0:
        heapq.heappush(heap,(-data,data))
    else:
        if heap:
            print(0)
        else:
            a=heapq.heappop(heap)
            print(a[1])    



