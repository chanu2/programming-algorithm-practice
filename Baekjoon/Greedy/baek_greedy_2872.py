import sys
n=int(sys.stdin.readline())
book=[]
max=0
cnt=0
for _ in range(n):
    book.append(int(sys.stdin.readline()))

max = book[0]    
for i in range(1,n): 
    if book[i] > max :
        if max+1 != book[i] :   # max를 구하는 코드 ** 
            max=book[i]
            cnt +=1
        max = book[i]
    else :
        cnt +=1
print(cnt)