#생성자가 없는 수를 셀프넘버라고 칭하고 있습니다
def self_number(n):
    sum=0
    n=str(n)
    for i in range(len(n)):
        sum+=int(n[i])
        a=int(n)+sum    
    return a
a=[x for x in range(1,10001)]
b=[]
for i in range(1,10001):
    c=self_number(i)
    b.append(c)

for j in a:
    print(a)    
   
for k in b:
    if k in a:
        a.remove(k)




