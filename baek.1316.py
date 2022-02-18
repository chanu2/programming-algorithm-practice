n=int(input())
word=[]
result=n
for _ in range(n):
    word.append(input())    
for i in range(n):
    for j in range(len(word[i])-1): #len(word[i])-1 --> 마지막 문자 생략 
        if word[i][j]==word[i][j+1]:   #문자가 연속으로 나오면 pass한다
            pass
        elif word[i][j] in word[i][j+1::]:
            result-=1                        # 같은 문자가 연속하지 않고 문자열 안에 같은것이 존재하면 결과값에 -1을 한다.
            break                             
print(result)        


        

