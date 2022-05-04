import sys
t=int(sys.stdin.readline())
result=[int(sys.stdin.readline())for _ in range(t)]   #컨프리헨션
wave=[0,1,1]    # 문제에서 인덱스 0 을 1로 시작 했기 때문에 인덱스 0 에 0을 추가
for i in range(100):    # 최대 수 
    wave.append(wave[i]+wave[i+1])    
[print(wave[k]) for k in result]    

