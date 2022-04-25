city=int(input())
distance=list(map(int,input().split()))  #map을 활용하여 리스트를 만든다
fuelprice=list(map(int,input().split()))   
i=1
miniprice=0
a=[]
minifee=fuelprice[0]*distance[0]   
while True:
    if i==len(distance):
        break
    elif fuelprice[i-1]>=fuelprice[i]:
        miniprice+=fuelprice[i]*distance[i]
        i+=1
    elif fuelprice[i-1]<fuelprice[i]:
        fuelprice[i]=fuelprice[i-1]    # if 조건을 만족한다면 현재값에 이전값을 넣어준다
        miniprice+=fuelprice[i]*distance[i]
        i+=1
print(miniprice)