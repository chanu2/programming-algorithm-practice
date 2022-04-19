a=[]
k=1
i=1
for _ in range(10):
    b=[int(x) for x in input().split()]
    a.append(b)

   
while True:
    while a[k][i]==0:
        a[k][i]=9
        i+=1
     
    if a[1+k][i-1]==0:
        a[1+k][i-1]=9
        k+=1


    elif a[k][i]==2:
        a[k][i]=9
        break
    elif a[1+k][i-1]==2:
        a[1+k][i-1]=9
        break
    if a[k][i]==1 and a[1+k][i-1]==1:
        break





    

   

for j in range(10):
    for l in range(10):
        print(a[j][l],end=" ")
    print()           
    
   






