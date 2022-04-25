import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data.sort()
print(data[(n-1)//2])
# averg=sum(data)/n
# for i in data:                    
#     a.append(abs(i-averg))           # 중앙값을 구해야 하는데 평균값을 구함
# print(data[a.index(min(a))])




