s=''
n=int(input())
for _ in range(n):         
    a=input().split()
    n1=int(a[0])   
    for i in range(len(a[1])):           # 각 문자를 정수와 곱한다.   EX) 'A'*3 = (AAA)    
        s+=a[1][i]*n1
    print(s)    
    s=''  
    


