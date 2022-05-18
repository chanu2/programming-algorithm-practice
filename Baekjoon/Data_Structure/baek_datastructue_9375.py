import sys
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    dic={}
    data=[]
    sum=1
    n=int(sys.stdin.readline().rstrip())
    for _ in range(n):
        num,kind=(sys.stdin.readline().split())
        data.append(kind)    # 종류의를 리스트에 추가한다
    for i in data:
        if i not in dic:     # 종류를 딕션어리 형태로 변환후 카운트 해준다
            dic[i]=1
        else:
            dic[i]+=1
            
    for i in dic:
        
        sum=sum*(dic[i]+1)    # 경우의 수를 구하는 코드
    print(sum-1)    




