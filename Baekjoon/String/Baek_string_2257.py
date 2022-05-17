import sys
ch=list(sys.stdin.readline().rstrip())
dic={'H': 1 ,'C': 12,'O': 16}   # 딕션어리로 만들어 준다.
stack=[]    # 빈 stack을 만들어 준다.
for i in range(len(ch)):  
    cnt=0     # cnt를 초기화 시킨다
    if ch[i]=='(':   
        stack.append(ch[i])   # stack에 괄호를 추가한다.
    elif ch[i] in dic:      # dic안에 있는 o,c,h 가 나온다면 
        stack.append(dic[ch[i]])    # dic vlaue 값을 stack에 추가한다.
    elif ch[i]==')':         # 닫힌 괄호가 나오면 
        while stack[-1] != '(':  # stack 안에 마지막이 ( 가 아닐때 반복문 실행

            cnt+= stack.pop() 
        
        stack.pop()
        stack.append(cnt)

    else:
        stack[-1]=stack[-1]*int(ch[i])  # dic션어리 안에 없으면 stack에 있는 마지막수에 곱하기 를 해준다.

print(sum(stack))