import sys
dic={}
s,e,q=map(str,sys.stdin.readline().split())
start=int(s[:2]+s[3:])
end=int(e[:2]+e[3:])          # 문자열 시간을 정수로 변환후 비교
qend=int(q[:2]+q[3:])
count=0
while True:
    
    try:
        
        time,user=map(str,sys.stdin.readline().split())
        
        
        if  int(time[:2]+time[3:]) <=start:    # 입장한 사람들 확인하는 코드
            dic[user]=1
        elif end <=int(time[:2]+time[3:]) <=qend:
            if user in dic:               #입장이 이미 확인된 사람들 기준으로 퇴장을 확인하는 코드
                dic[user]+=1
    except:
        break                        # 예외처리 얼마나 입력받을지 모를 때 사용할 수 있다.
for i in dic:
    if dic[i]>=2:
        count+=1
print(count) 

    
