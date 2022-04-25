import sys
i=1
while True:
    perfect=sys.stdin.readline()
    cnt=0
    if '-' in perfect:    #-을 입력 받으면 프로그래램 종료
        exit()
    while True:
        if len(perfect)==0:
            print('%d. %d'%(i,cnt))
            break
        if perfect[0]=='}':
            perfect='{'+ perfect[1:]    # 항상 첫번째는 { 이며 마지막은 } 이다.
            cnt+=1
        if perfect[-1]=='{':
            perfect=perfect[:-1]+'}'
            cnt+=1    
        perfect=perfect.replace('{}','').strip() #문자열 안에 원하는 문자를 찾고 변환해주는 모듈
    i+=1
   

             

