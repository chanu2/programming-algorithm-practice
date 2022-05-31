import sys

n = int(sys.stdin.readline())
entrance = {}
exit = []
cnt = 0


for i in range(n):
    entrance[(sys.stdin.readline().rstrip())] = i

#나간 차를 리스트에 입력 받음
for _ in range(n):
    exit.append(sys.stdin.readline().rstrip())

for j in range(n-1):  # 막지막 리스트요소는 뽑을 필요가 없기 때문에
    for k in range(j+1,n):
        # 제일 먼저 나간 차의 들어간 순번 > 그 다음으로 나간 차의 들어간 순번
        if entrance[exit[j]] > entrance[exit[k]]:
            cnt += 1
            break
print(cnt)
      

    