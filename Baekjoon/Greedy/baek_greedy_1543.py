word=input()
findword=input()   #word.find(findword,시작인덱스, 끝인덱스)  
cnt=0 
i=word.find(findword)
if i==-1:
    print(cnt)
    exit()
cnt+=1   
while True:
    i=word.find(findword,i+len(findword))
    if i==-1:
        print(cnt)
        break
    else:
        cnt+=1
    

