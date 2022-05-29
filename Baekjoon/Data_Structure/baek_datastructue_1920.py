#이진 탐색을 이용한 문제 
# 정렬되있는 상태에서 logn을 보장한다

import sys

def binarySearch(array,target,start,end):
    while start<=end:   # 반복문 조건
        mid=(start+end)//2    # 중간 인덱스를 찾는 코드

        if array[mid]==target:    # 중간 인덱스의 array가 target이면 존재하고 1을 반환
            return 1
        elif array[mid]>target:   # 중간 인덱스의 array값이 target보다 크면 end 포함 이후에는 볼 필요가 없다.   
            end=mid-1
        else:
            start=mid+1
    return 0                

n=int(sys.stdin.readline())
data1=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
data2=list(map(int,sys.stdin.readline().split()))
data1.sort()   # 오름차순 정렬해주는 코드

for i in data2:
    print(binarySearch(data1,i,0,n-1))

