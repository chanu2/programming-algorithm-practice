n=input()
sum=1
if n[0]==' 'and n[len(n)-1]!=' ':
    for i in range(1,len(n)):
        if n[i]==' ':
            sum+=1
    print(sum)       
          
elif n[0]!=' 'and n[len(n)-1] ==' ':
    for j in range(len(n)-1):
        if n[j]==' ':
            sum+=1
    print(sum)        
elif n[0]!=' 'and n[len(n)-1]!=' ':
    for l in range(len(n)):
        if n[l]==' ':
            sum+=1
    print(sum)       

elif n[0]==' ':
    print(0) 


