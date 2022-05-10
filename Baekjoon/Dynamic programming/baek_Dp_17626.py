import sys
n=int(sys.stdin.readline())
Dp=[0]    

for i in range(1,n+1):
    mini_result=1e9   #10**9을 나태내는 코드
    j=1

    while j**2<=i:
        mini_result=min(mini_result,Dp[i-j**2])   
        j+=1
    Dp.append(mini_result+1)
print(Dp[n])        