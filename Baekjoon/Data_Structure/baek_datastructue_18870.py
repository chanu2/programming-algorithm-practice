import sys    # 딕션어리를 통해서 시간복잡도를 낮춘다
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split())) 
a=list(set(data))   # 중복을 제거한다
a=sorted(a)
dic={a[i]: i for i in range(len(a))} # 딕션어리 컴프리헨션  # 딕션어리 선언 

for k in data:
    print(dic[k],end=' ')   