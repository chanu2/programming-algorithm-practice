n=input()
sum=0
for i in range(len(n)-1):
    if n[0]=='0':
        if n[i]=='0' and n[i+1]=='1':
            sum+=1
            
    elif n[0]=='1':
        if n[i]=='1' and n[i+1]=='0':
            sum+=1  
    elif n not in '0' and n not in '1':
        sum=0      
print(sum)