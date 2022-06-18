import sys
n,m=map(int,sys.stdin.readline().split())
dic={}   # 딕션어리 선언
cnt=0
answer=[]  # 결과를 출력할 변수를 리스트로 선언
for i in range(n):
    name1=sys.stdin.readline().rstrip()
    dic[name1]=1  
for j in range(m):
    name2=sys.stdin.readline().rstrip()
    if name2 in dic:  # 이미 dic에 key값으로 name2가 존재할 때
      cnt+=1  # 카운트
      answer.append(name2)   # 결과 리스트에 추가한다
answer.sort()      # 사전순으로 정렬하는 코드
print(cnt)                    
for k in answer:   # 출력
    print(k)
  
    




       

        

