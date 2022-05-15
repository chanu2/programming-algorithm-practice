import heapq
import sys
n=int(sys.stdin.readline())
positive=[]   # 양수를 받았을 때 
negative=[]   # 음수를 받았을 떄
for i in range(n):
    component=int(sys.stdin.readline())
    if component>0:   
        heapq.heappush(positive,component)
    elif component<0:     # 음수를 받으면 -를 붙여서 양수로 받아준다
        heapq.heappush(negative,-component)    
    else:
        if not positive: # positive가 비어있다면
            if not negative: # negative가 비어있다면
                print(0)
            
            else:
                print(-(heapq.heappop(negative)))   # p는 비었지만 n이 비어있지 않을 때(heappop을 통해서 가장 작은 값을 반환하고 *-1을 해준다 )
        elif not negative:        # p 가 존재하고 n은 비어있을 때
            print(heapq.heappop(positive))

        else:         # p와 n이 둘다 존재할 때
            a= heapq.heappop(positive)   # 인자를 받아준다
            b= -heapq.heappop(negative)   # 음수를 붙여준다

            if abs(a)<abs(b):        # 절대값이 n이 클 때
                print(a)
                heapq.heappush(negative,-b)
            else:
                print(b)             # 절대값에서 p 가 크거나 같을 때
                heapq.heappush(positive,a)



########   더 빠른 방법 힙큐에 값을 넣을 때 (절대값, 원래값) 쌍으로 넣어줄 수 있다. 
# 또한 절대값을 기준으로 정렬을 할 수 있게 할 수 있다.


# import heapq
# import sys
# n=int(sys.stdin.readline())
# q=[]
# for i in range(n):
#     a=int(sys.stdin.readline().rstrip())
#     if a!=0:
#         heapq.heappush(q,(abs(a),a))
#     else:
#         if not q:
#             print(0)
#         else:
#             print(heapq.heappop(q[1]))    



         
