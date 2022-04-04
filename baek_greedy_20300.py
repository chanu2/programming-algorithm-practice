import sys
machine_kind=int(sys.stdin.readline()) 
result=0
loss_muscle=list(map(int,sys.stdin.readline().split()))
loss_muscle.sort() # 오름차순으로 정렬
if machine_kind%2==0:   # 짝수 홀수 구별하는 코드
    result=loss_muscle[0]+loss_muscle[len(loss_muscle)-1]
    for i in range(1,len(loss_muscle)//2):  
        if result<loss_muscle[i]+loss_muscle[len(loss_muscle)-(i+1)]: # 짝수 일때 리스트 내부의 첫번째 요소와 마지막요소를 더해서 비교하여 최대값을 구하는 코드
            result=loss_muscle[i]+loss_muscle[len(loss_muscle)-(i+1)]
    print(result)
else:
    a=loss_muscle.pop() # 홀수일때 리스트 내부 마지막요소를 pop()을 통해 리스트길이를 짝수로 변경
    result=loss_muscle[0]+loss_muscle[len(loss_muscle)-1]
    for i in range(1,len(loss_muscle)//2):
        if result<loss_muscle[i]+loss_muscle[len(loss_muscle)-(i+1)]: # 짝수 일때 리스트 내부의 첫번째 요소와 마지막요소를 더해서 비교하여 최대값을 구하는 코드
            result=loss_muscle[i]+loss_muscle[len(loss_muscle)-(i+1)]
    if a>result:   # 만약에 pop()했던 요소가 가장크다면 그 요소를 출력
        print(a)   
    else:
        print(result)    
