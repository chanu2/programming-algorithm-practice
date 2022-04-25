package=[]
single=[]
mini=0
n,m=map(int,input().split())
for _ in range(m):
    a,b=map(int,input().split())
    package.append(a)
    single.append(b)
if min(package)>=6*min(single):
    print(n*min(single))
    exit()

else:
    mini+=(n//6)*min(package)
if (n%6)*min(single)>=min(package):
    mini+=min(package)
else:
    mini+=(n%6)*min(single)
print(mini)    


