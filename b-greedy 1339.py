import sys
n=int(int(sys.stdin.readline()))
sum=[]
result=0
dic={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'N':0,'M':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0} #딕셔너리를 선언한다 
word = [list(input()) for _ in range(n)]

for i in word:
    for j in range(len(i)):
        num=10**(len(i)-j-1)  # 자릿수를 더하는 코드
        dic[i[j]]+=num

for i in dic.values():   #딕셔너리 values 값만을 나타내는 코드
    sum.append(i)

sum.sort(reverse=True)  # 내림차순으로 정렬

for i in range(9):
    result+=sum[i]*(9-i)
print(result)    








            




        
            


