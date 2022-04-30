import sys
while True:
    sin=list(map(int,sys.stdin.readline().strip()))
    if sum(sin)==0:   #입력에 0만 존재하면 프로그램 종료
        break

    a=list(reversed(sin))   #리스트 거꾸로 뒤집기
    if sin==a:  
        print('yes')
        
    else:
        print('no')
   



