import sys
n,m=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))

#이진 탐색을 이용한 문제 해결
result=0    # 최종값을 나타낸다.
start=0     #시작 인덱스
end=max(tree)   # 마지막 인덱스

while start<=end:      
    total=0     # 나무를 잘랐을 때 나머지들 합
    mid=(end+start)//2    # 중간값을 정해서 나무를 자르는 높이
    for i in tree:        
        if i>mid:         # i값이 mid 값보다 클때 나무에서 톱 높이 만큼 자른 나머지가 나온다.
            total+=i-mid   
    if total<m:           # 자른 나무의 합이 원하는 값 보다 작다는 것은 mid(나무를 자르는 높이)가 높다는 뜻이고 그이후의 높이는 생각할 필요가 없다.                      
        end=mid-1         # end를 줄여준다
        
    else:
        result=mid        # mid값을 저장해주고
        start=mid+1       # mid값 이전 인덱스들은 생각할 필요가 없기 때문에 start에 mid+1을 대입해준다
    
    #if total>=m:            # 이코드를 쓰면 시간초과가 발생한다. 
       #result=mid    
       # start=mid+1
    #else:
       #end=mid-1      
        
print(result)            




