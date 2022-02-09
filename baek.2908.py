data= input().split()  
sum1=''
sum2=''
for i in range(2,-1,-1):
    sum1+=data[0][i]
    sum2+=data[1][i]
if int(sum1)>int(sum2):
    print(sum1)
else:
    print(sum2)        
