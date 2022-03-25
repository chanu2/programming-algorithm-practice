import sys
shortcutkeys=[]
flag=False
n=int(sys.stdin.readline())
for _ in range(n):
    
    option=list(map(str,sys.stdin.readline().split()))

    for i in range(len(option)):
        if option[i][0].upper() not in shortcutkeys:
            shortcutkeys.append(option[i][0].upper())
            option[i]="["+option[i][0]+"]"+ option[i][1:]
            print(" ".join(option))  #'구분자'.join(리스트) 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수
            break
    
    else:
        flag=False #반복문이 break 를 통과하지 않았다면 ---> 예외처리 느낌과 비슷 for문에 걸리는 else   

        for j in range(len(option)):
            
            for k in range(len(option[j])):
                if option[j][k].upper() not in shortcutkeys:
                    shortcutkeys.append(option[j][k].upper())
                    flag=True
                    option[j]= option[j][:k]+"["+option[j][k]+"]"+option[j][k+1:]
                    print(" ".join(option))
                    break
    
            if flag==True: # 첫번째 for문을 나가기 위한 코드
               break
        
        else:
            print(" ".join(option))      








