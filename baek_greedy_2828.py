position=[]
n,m=map(int,input().split())
applenumber=int(input())
for _ in range(applenumber):
    position.append(int(input()))
end=m
start=1
move=0    
for i in range(len(position)):
    if end>=position[i] and start<=position[i]:   # 끝위치와 처음 위치 안에 사과의 위치가 존재할 때
        pass
    elif position[i]>end:
        move+=position[i]-end # 사과의 위치가 끝 위치보다 클떄
        end=position[i]
        start=end-(m-1)
    elif position[i]<start:
        move+=start-position[i] # 사과의 위치가 처음 위치보다 작을때
        start=position[i]
        end=start+(m-1)
    
print(move)        


