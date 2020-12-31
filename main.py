from sys import stdin
N,M=map(int,stdin.readline().strip().split())
li=[list(map(int,stdin.readline().strip().split())) for i in range(N)]
dp=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j]=li[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2=map(int,stdin.readline().strip().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
