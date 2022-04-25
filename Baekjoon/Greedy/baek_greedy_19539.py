import sys
n=int(sys.stdin.readline())
tree=list(map(int,sys.stdin.readline().split()))
if sum(tree)%3==0:
    bottle2=sum(tree)//3       # 합이 3의 배수인지 확인
    
else:
    print('NO')
    exit()    
tree.sort(reverse=True)     # 내림차순 정렬
for i in range(n):
    if tree[i]<2 and  bottle2!=0:    # 종료 조건
        print('NO')
        break
    elif tree[i]//2<=bottle2:
        bottle2=bottle2-tree[i]//2    #리스트의 요소를 확인하여 bottle2의 카운터를 줄여주는 코드 
        tree[i]=tree[i]%2
        if bottle2==0:
            print('YES')
            break

    else:
        print('YES')
        break

    
# 더 간단한 코드 
 
# n = int(input())
# T = list(map(int, input().split()))
# T_sum = sum(T)
# A = T_sum // 3

# if T_sum % 3 != 0:   
#     print('NO')
                                 
# else:
#     for i in T:
#         A -= (i // 2)          # 각항을 나누면서 몫만을 고려한 코드
#     if A > 0:                  # 2를 먼저 모두 사용하며 1은 사용 할 필요가 없다.
#         print('NO') 
#     else:
#         print('YES')





   