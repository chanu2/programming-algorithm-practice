import sys
pd=sys.stdin.readline().split()
for i in range(len(pd)):      
    if pd[i::]==pd[i::][::-1]:   # 문자열 과 리스트를 슬라이싱 할때 #pd[i::][::-1]의 뜻은 문자열을 두번 슬라이싱 할 수 있다.
        print(len(pd)+i)     # i부터 끝까지 문자열을 슬라이싱하고 [::-1] 문자열을 뒤집어준다.

