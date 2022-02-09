data= input().split()
#a=data[0][2]+data[0][1]+data[0][0]
#b=data[1][2]+data[1][1]+data[1][0]      
#a=int(a)
#b=int(b)
#if a>b:
    #print(a)
#else:
    #print(b)    
sum1=''
sum2=''
for i in range(2,-1,-1):
    sum1+=data[0][i]
    sum2+=data[1][i]
if int(sum1)>int(sum2):
    print(sum1)
else:
    print(sum2)        
