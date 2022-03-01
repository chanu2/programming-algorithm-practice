rope=[]
maxweight=[]
n=int(input())
for _ in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)       #내림차순으로 정렬 리스트 자체를 변환한다 
                              # list.reverse() : list 자체를 역순으로 정렬, 함수 반환값 None 값
                              # reversed(list) : 역순 정렬된 list 새로운 변수에 할당 가능   //sort와 sorted함수와 유사하다
for i in range(len(rope)):
    maxweight.append(rope[i]*(i+1))
print(max(maxweight))         # 최대값을 찾는다



