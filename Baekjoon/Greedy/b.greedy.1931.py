# 회의시간 배정하기
n=int(input())
space=[]
for i in range(n):                 
    a,b=map(int,input().split())
    space.append([a,b])


space.sort(key=lambda x:x[0])  #space.sort(key=lambda x:x[0]) # space 리스트를 x[0]으로 정렬(회의가 빨리 시작하는 순서로 정렬) 

space.sort(key=lambda x:x[1])  #space.sort(key=lambda x:x[1]) # space 리스트를 x[1]으로 정렬(회의가 빨리 끝나는 순서로 정렬) 


count=1
end_time=space[0][1]
for j in range(1,n):
    if end_time <= space[j][0]:  # 회의 종료 시간과 다음 회의 시작 시간과 비교
        count+=1
        end_time=space[j][1]

print(count)

 