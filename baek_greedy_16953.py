import sys
a,b=map(str,sys.stdin.readline().split())
cnt=0
while True:   # 무한 반복
    if int(b)==int(a):   
        print(cnt+1)   #a==b가 같아지는 순간 종료
        break
    elif int(b)<int(a): # b를 2로 나누고 b의 1을 제거 하면서 a가 b보다 더 커지면 실행    
        print(-1)       
        break
    elif b[-1]=='1':
        b=b[:-1]   # 1을 제거해주는 코드
        cnt+=1
    
    else:
        if int(b)%2==0:
            b=str((int(b)//2))   
            cnt+=1         
        else:
            print(-1)     # 홀수이면서 끝자리수가 1이 아닌 수를 입력 받았을 때 실행되는 코드
            break    

