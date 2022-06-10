import sys
num=list(map(str,sys.stdin.readline().rstrip()))
num.sort(reverse=True)  # 오름차순 정렬
print(''.join(num))  # 리스트를 붙여서 문자열로 반환해 주는 코드
