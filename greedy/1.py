h,w=(input().split())
a=[[0 for _ in range(int(w))]for _ in range(int(h))]
print(a)
n=int(input())
for _ in range(n):
    l,c,x,y=(input().split())
    if int(c)==0:
        for i in range(int(l)):
            a[int(x)-1][int(y)-1+i]=1
    else:
        for j in range(int(l)):
            a[int(x)+j-1][int(y)-1]=1

for k in range(int(h)):
    for g in range(int(w)):
        print(a[k][g],end=' ')
    print()    





    





#for i in range(3):
    #a=[int(x) for x in input().split()]
    
#print(a[1][1])    


