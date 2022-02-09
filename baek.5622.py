n=input()
sum=0
alphabet=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P',
'Q','R','S'],['T','U','V'],['W','X','Y','Z']]
for i in n:
    for j in range(len(alphabet)):
        if i in alphabet[j]:   # alphabet[j]안에 입력받은 i가 존재하면 {(j+3)을 더한다-->번호하나를 누르는데 걸리는 시간} 
            sum+=(j+3)
print(sum)            


    
