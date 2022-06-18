import sys
input=sys.stdin.readline
n=int(input())
series=665
cnt=0
while True:
    series+=1     # 665에서 계속 1씩 더해준다.   브루트포스 알고리즘 
    if '666' in str(series):   # series안에 최소한 '666'이 있는지 확인하고 카운트해준다.
        cnt+=1
    if cnt == n:  # break조건 
        print(series)
        break    
    


  
    




       

        

