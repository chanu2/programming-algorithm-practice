import sys
n,m=map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))
card.sort(reverse=True) #내림차순 정렬
for _ in range(m):
    a=card.pop()
    b=card.pop()  # 가장 작은 두 수 완전히 빼오기
    card.append(a+b)
    card.append(a+b)    # 두 수를 더해서 리스트에 다시 append
    card.sort(reverse=True)   

print(sum(card))     # 리스트 합 출력
