sum=''
n=list(input())
n.sort(reverse=True)
for i in range(len(n)):
    sum+=n[i]
if int(sum)%30!=0:
    print(-1)
else:
    print(sum)        
    


