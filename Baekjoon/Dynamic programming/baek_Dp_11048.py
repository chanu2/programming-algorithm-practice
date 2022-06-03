import sys
n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

dp=[[0]*(m+1) for _ in range(n+1)]  # dp를 하나 생성해줘야 한다.

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+graph[i-1][j-1]
print(dp[n][m])

