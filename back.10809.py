a=list(input())
b=[]
c=[]
for j in range(97,123):
    b.append(chr(j))
    c.append(chr(j))
for k in range(len(a)):
    for i in range(26):
        if a[k]==b[i]:
            b[i]=k

for p in range(26):
    if b[p]==c[p]:
        b[p]=-1
for q in b:
    print(q,end=' ')                                                 


# python  find함수를 이용!  (str.find('찾을 값')) -> 찾을 값의 인덱스를 반환한다 없다면 -1을 반환한다
# str=input()
# al='abcdefghijklmnopqrstuvwxyz'
# for i in al:
     # print(str.find(i),end=' ')
      
     

     





