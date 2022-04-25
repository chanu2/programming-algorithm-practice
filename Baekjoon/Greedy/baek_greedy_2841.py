import sys
n,p=map(int,sys.stdin.readline().split())
string=[[] for _ in range(6)]   #기타 6줄을 만드는 코드
cnt=0
for i in range(n):
    s,p=map(int,sys.stdin.readline().split())
    if len(string[s-1])==0:     # 어떤 기타줄에 아무 플렛을 잡지 않았을 때
        string[s-1].append(p)
        cnt+=1
    else:
        if string[s-1][-1]<p:   # 어떤 기타줄에 플렛이 이미 존재하고 추가할 플랫보다 클 때
            string[s-1].append(p)
            cnt+=1
        elif string[s-1][-1]==p:   #어떤 기타줄에 플렛이 이미 존재하고 추가할 플렛과 깉을 때
            pass
        else:   ##어떤 기타줄에 플렛이 이미 존재하고 추가할 플렛보다 작을 때
            while len(string[s-1])!=0 and string[s-1][-1]>p:  # 추가 할 플렛 보다 큰수를 제거하는 코드 
                string[s-1].pop()
                cnt+=1

            if len(string[s-1])!=0 and string[s-1][-1]==p:   # 추가 할 플렛 보다 큰수를 제거하다가 같은 수가 나왔을 때 실행되는 코드
                pass
            else:
                string[s-1].append(p)  
                cnt+=1    

print(cnt)



