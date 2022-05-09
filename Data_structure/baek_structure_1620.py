import sys
n,m=map(int,sys.stdin.readline().split())
name={}   # 딕션어리 만들기 2개 만들기 key 값과 value값 자유롭게 이용하기 위해
number={}
for i in range(n):
    data=sys.stdin.readline().strip()
    name[data]=i+1       # 딕션어리에 key 값과 value값을 추가한다.
    number[i+1]=data     #

 
for _ in range(m):
    find_data = sys.stdin.readline().strip()
    try:                        #예외처리 try에서 오류가 발생한다면 사전에 어떤 오류가 발생할지 미리 확인한 후
                                # except문을 실행한다. 만약 try문에 오류가 발생하지 않으면 except문을 실행하지 않는다.
        a=int(find_data)
        print(number[a])        #입력받은 문자가 정수로 변환 가능할때
    except ValueError:
	    print(name[find_data])   