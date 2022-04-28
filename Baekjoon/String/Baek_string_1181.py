import sys
n=int(sys.stdin.readline())
dic=[(sys.stdin.readline().strip())for _ in range(n)]  # 컨프리핸션을 이용한 표현
dic=list(set(dic))  # 중복을 제거
dic.sort() # 알파벳 순으로 정렬
dic=sorted(dic,key=len) # 길이를 기준으로 정렬
for i in dic:
    print(i)