
a=input().split('-')    # 받은 문자열을 '-'로 나눈다
number=[]    
for i in a:
    sum=0
    e=i.split('+')      
    for j in e:
        sum+=int(j)   
    number.append(sum)
n=number[0]         # 첫번째 배열은 항상 +이므로 number[0]을 넣어준다
for i in range(1,len(number)):
    n-=number[i]      

print(n)    


                    
        



     
        

    


