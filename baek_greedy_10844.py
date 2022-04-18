import sys
n=int(sys.stdin.readline())
data1=list(map(int,input().split()))
data2=[]
data3=[]
result1=[]
result2=[]
result3=[]
a=[]
for i in data1:
    data2.append(i)
for i in data1:
    data3.append(i)
    
data1[0]=0

for i in range(1,len(data1)-1):
    result1.append((sum(data1[i+1::]*2)+sum(data1[:i])))
   

a.append(max(result1))


data2[-1]=0
data2.reverse()
for j in range(1,len(data2)-1):
    result2.append((sum(data2[j+1::]*2)+sum(data2[:j])))

a.append(max(result2)) 


k=max(data3[1:len(data3)-1])
k=data3.index(k)

a.append(sum(data3[1:k+1])+sum(data3[k:len(data3)-1]))


print(max(a))




