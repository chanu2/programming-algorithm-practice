import sys
input=sys.stdin.readline
n,m=map(int,input().split())
chess=[list(map(str,input().strip())) for i in range(n)]
print(chess)
result=[]
for i in range(n-7):
    for j in range(m-7):
        b=0 # B로 시작했을 때 B를 색칠해야하는 개수
        w=0 # W로 시작했을 때 W를 색칠해야하는 개수
        for k in range(i,i+8):
            for p in range(j,j+8):

                # 짝수라면
                if (k+p)%2==0:
                    # W니깐 B가 되야하니 색칠
                    if chess[k][p]=='W':
                        b+=1 # B로 시작!
                        
                    # B니깐 W가 되야하니 W 색칠
                    if chess[k][p]=='B':
                        w+=1
                        
                # 홀수라면
                else:
                    # 시작이 W 가정, B니깐 색칠
                    if chess[k][p]=='B':
                        b+=1
                    
                    # 시작이 B 가정, W니깐 색칠
                    if chess[k][p]=='W':
                        w+=1        
        result.append(b)
        result.append(w)

print(result)
print(min(result))











            
