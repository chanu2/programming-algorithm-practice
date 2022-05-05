# import sys                    ##### 시간 초과 다음번에는 뉴클리드 호재법으로 풀어보기!!!!!!
# N,M=map(int,sys.stdin.readline().split())

# #최소 공약수
# for i in range (min(N, M), 0, -1):   # (N,M)둘 중 작은것 부터 1까지
#     if N%i == 0 and M%i == 0: 
#         print(i)
#         break
                                                                                    
# # 최소공배수
# for i in range (max(N,M), (N*M)+1):   # (N,M)둘 중 큰 수 부터 최소공배수의 최대값인 N*M까지
#     if i % N == 0 and i % M == 0:
#         print(i)
#         break


import math         # 모듈을 사용한 코드
import sys
a, b = map(int, sys.stdin.readline().split())   
print(math.gcd(a,b))
print(math.lcm(a,b))