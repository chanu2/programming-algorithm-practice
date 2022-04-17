import sys
T=int(sys.stdin.readline())
for _ in range(T):

    n=int(sys.stdin.readline())
    tree=list(map(int,sys.stdin.readline().split()))
    tree.sort(reverse=True)    #내림차순정렬
    result=[]
    max=0
    for i in range(len(tree)):
        if i%2==0:
            result.insert(0,tree[i])     #큰수를 가장 중간에 두고 그다음 큰수를 왼쪽 오른쪽에 정렬하는 코드
        else:
            result.append(tree[i])              
    for i in range(len(result)-1):
        if max < abs(result[i]-result[i+1]):   #차이를 이용해 최대값을 출력
            max = abs(result[i]-result[i+1])
    print(max)            
# reveiw 코드가 너무 길고 지저분함 알고리즘 적으로 간단하게 생각해야함!

# 간단한 코드 

# import sys
# T=int(sys.stdin.readline())
# for _ in range(T):

#     n=int(sys.stdin.readline())
#     tree=list(map(int,sys.stdin.readline().split()))
#     tree.sort()                                      #오름차순정렬 
#     result=0
#     for i in range(2,n): 
#         result=max(result,abs(tree[i]-tree[i-2]))    # 인덱스가 2 차이가 날때 가장 작은 차를 가진다
                                                       # 만약 나무 5개있다면 정렬하면 [4,2,1,3,5]이런 순서의 인덱스를 가져야한다.
                                                       # 인덱스 차이를 2로 해준다.
#     print(result)    