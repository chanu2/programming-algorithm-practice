import sys
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    stack=[]
    data=list(sys.stdin.readline().strip())

    for i in data:
        
        if i=='(':
            stack.append(i)
        else:
            if not stack:    # 스택이 비어있을 때
                print('NO')
                break
            else:
                stack.pop()
    else:         #for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고, 끝까지 수행 되었을 때 수행하는 코드
        if stack:
            print('NO')
        else:
            print('YES')                 

     

                
                   
                
            