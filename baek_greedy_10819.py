# import sys                                            # 가장 작은값을 중심으로 양쪽에 가장 큰값 그다음 양쪽에 가장 작은 값 들을 정렬하려했다.
                                                        # 입력을 [20, 1 ,15, 8, 4, 10]   --> 정렬 후 -->    [4,10,20,1,15,8]
                                                        # 반례 [100,41,1]
# n=int(input())                                        ##### 느낀점 ######
# array=list(map(int,sys.stdin.readline().split()))     # 알고리즘 문제를 풀면서 단번에 정답을 도출하는 알고리즘을 생각하는 법과 시간복잡도를 계산해보고 모든 경우의 수를 찾아 코드를 작성하는 법의 합의점을 장 찾아야겠다.
# answer=0
# array.sort(reverse=True)
# result=[]
# result.append(array.pop())
# data1=[array[i] for i in range(0,len(array),2)]
# data2=[array[i] for i in range(1,len(array),2)]
# if len(data1)==len(data2):
#     while len(data2)!=0:
#         result.insert(0,data1.pop(0))
#         result.append(data2.pop(0))
#         if len(data2)==0:
#             break
#         else:
#             result.insert(0,data1.pop())
#             result.append(data2.pop()) 
# else:
#     while len(data2)!=0:
#         result.insert(0,data1.pop(0))
#         result.append(data2.pop(0))
#         if len(data2)==0:
#             break
#         else:
#             result.insert(0,data1.pop())
#             result.append(data2.pop())
#     result.insert(0,data1.pop())
# for i in range(len(result)-1):
#     answer+=abs(result[i]-result[i+1])

# print(answer)    

from itertools import permutations    # 순열 
import sys
 

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
 
per = permutations(a)    # 순열 라이브러리
ans = 0
 
for i in per:
    s = 0
    for j in range(len(i)-1):              
        s += abs(i[j]-i[j+1])   
    if s > ans:      ## 최대값을 찾는 코드
        ans = s
 
print(ans)       
    


