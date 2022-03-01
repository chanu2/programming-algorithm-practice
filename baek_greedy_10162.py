n=int(input())
button=[300,60,10]
for i in range(len(button)):
    a=0
    if n%10!=0:
        print(-1)
        break
    elif n//button[i]>0:
        a=n//button[i]
        n-=a*button[i]
        print(a,end=' ')
    else:
        print(a,end=' ')
# 더빠른 방법
# ex) 100//300=0, 100%300=100, 100/300=0.3 
# n=int(input())
# if n%10 !=0:
#     print(-1)
# else:
#     a=0
#     b=0
#     c=0
#     a=n//300
#     b=(n%300)//60
#     c=((n%300)%60)//10
#     print(a,b,c)