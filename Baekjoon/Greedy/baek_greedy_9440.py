import sys
a=[]
A=[]
B=[]
result1=''
result2=''
data=list(sys.stdin.readline().split())
if data[0]=='0':
    exit()
data.pop(0)
for i in range(len(data)):
    if data[i]=='0':
        a.append(data[i])


if len(a)==0:
    data.sort()
    
    for i in range(0,len(data),2):
        result1+=data[i]
    for i in range(1,len(data),2):
        result2+=data[i]
    print(int(result1)+int(result2))       

else:

    rm_set = ['0']
    data = [i for i in data if i not in rm_set]
    data.sort()
   
    result1=data.pop(0)
    result2=data.pop(0)
    for i in range(len(a)):
        data.insert(i,a[i])
  
    for i in range(0,len(data),2):
        result1+=data[i]
     
    
    for i in range(1,len(data),2):
        result2+=data[i]
   
    print(int(result1)+int(result2))
  
