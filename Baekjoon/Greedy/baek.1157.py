a=list(input())
b=[]
c=[]

for i in a:
    b.append(i.upper())   # 입력받은 리스트를 대문자로 변환
a.clear()
d=list(set(b))           # 중복을 제거

for j in d:    
    a=b.count(j)     # 입력받은 리스트 안의 요소의 각 갯수를 새로운 리스트에 저장
    c.append(a)

for k in range(len(c)):
    if c.count(max(c))!=1:          # 최대 값이 1개가 아니라면 ?를 출력한다.
        print("?")
        break
    elif c[k]==max(c):    
        print(d[k])                   #갯수를 저장한 리스트에서 최대값을 찾는다