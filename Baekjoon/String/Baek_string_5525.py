import sys
n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
s=sys.stdin.readline().strip()
cnt=0    # 'IOI'개수
result=0   # 원하는 PN에서 N의 개수
i=0           
while i<m-1:       
    if s[i:i+3]=='IOI':
        cnt+=1    # 'IOI'를 발견하고 카운트
        i+=2      # P는 IOIOIOI... 이런 꼴이기 때문에 인덱스 +2를 해준다.
        if cnt==n:    # cnt 와 n의 개수가 같으면 찾고 싶은 문자를 찾은 상태
            result+=1   
            cnt-=1    # s를 겹치면서 연쇄적으로 확인 해야하기 때문에 -1을 해준다. 
    else:
        i+=1      # IOI를 찾지 못했을 때
        cnt=0     # cnt 초기화

print(result)
            


