import sys
n=int(sys.stdin.readline())
data=[]
cnt=0

for _ in range(n):
    data.append(sys.stdin.readline().rstrip())  

for i in range(n-1):   
    for j in range(i+1,n):
        dic={}
        for k in range(len(data[0])):  # 주어진 단어 길이 만큼 반복한다.
            
            if data[i][k]==data[j][k]:    
                if data[i][k] not in dic:   # dic에 이미 요소가 있는지 없는지 확인한다.   
                    dic[data[i][k]]=data[j][k]     # 없다면 dic안에 요소를 추가해준다
                    
                    
                else:
                    if dic[data[i][k]]!=data[j][k]:
                        break    # dic안에 이미 요소가 있고 그 때 value값이 다르면 break
                        
            else:
                if data[i][k] not in dic: 
                    dic[data[i][k]]=data[j][k]
                    
                else:
                    if dic[data[i][k]]!=data[j][k]:
                        break
                  
        else:   # 위에 for문에 break에 걸리지 않았을 때

            a=(list(dic.values()))     # 벨류 값들을 리스트로 만들고
            b=list(set(a))       # ex) ab 와 cc 를 비교한다 가정하면 dic={a:'c',b:'c'} 이기 때문에

            
            if len(a)==len(b): # 벨류 값에 중복이 있는 지 확인 하는 코드
                cnt+=1 
print(cnt)           
                    




    
