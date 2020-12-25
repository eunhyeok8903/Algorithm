from sys import stdin

S1=stdin.readline().rstrip()
S2=stdin.readline().rstrip()
S3=stdin.readline().rstrip()

len1=len(S1)
len2=len(S2)
len3=len(S3)

dp=[[[0]*(len1+1) for _ in range(len2+1)] for _ in range(len3+1)]
for i in range(1,len1+1):
    for j in range(1,len2+1):
        for k in range(1,len3+1):
            if S1[i-1]==S2[j-1]==S3[k-1]:
                dp[k][j][i]=dp[k-1][j-1][i-1]+1
            else:
                dp[k][j][i]=max(dp[k-1][j][i],dp[k][j-1][i],dp[k][j][i-1])

print(dp[-1][-1][-1])
"""
3차원 배열
[높][세][가]
dp=[[[0]*(len1+1) for _ in range(len2+1)] for _ in range(len3+1)] // 가로 세로 높이



"""