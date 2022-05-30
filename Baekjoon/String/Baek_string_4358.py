import sys
dic={}
cnt=0
while True:
    data=sys.stdin.readline().rstrip()

    if data!='':     
        cnt+=1
        if data in dic:
            dic[data]+=1 
        else:
            dic[data]=1
            
    else:
        break  
dic1=sorted(dic)   # 사전순으로 정렬된다.
for i in dic1:
    print(i,'{:.4f}'.format((dic[i]/cnt)*100))  #format을 이용한 4자리수까지 반올림

   