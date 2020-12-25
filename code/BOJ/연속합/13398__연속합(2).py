N= int(input())
arr=list(map(int,input().split(' ')))
dp=[[-1001 for i in range(N)] for raw in range(2)]
result=-1001
dp[0][0]=arr[0]
dp[1][0]=max(arr[0],result)
result=max(dp[0][0],dp[1][0])
for i in range(1,N):
    dp[0][i]=max(dp[0][i-1]+arr[i],arr[i])
    dp[1][i]=max(dp[1][i-1]+arr[i],arr[i],dp[0][i-1])
    result=max(result,dp[0][i],dp[1][i])
print(result)

"""
문제:
구간합 최대문제(단 여기서 1개 인덱스를 지울 수 있다, 안지워도 됨)
인덱스 하나하나 다 지워보면서 dp를 구하게 되면 10만*10만 (N^2)으로 시간초과가 뜬다

그래서 한가지 원소 지우는 경우도 dp를 해결하는 점화식에 녹아내릴 필요가 있다.
이런경우는(BFS에서 벽을 부순 경우 안부순 경우 나누는 문제 기초가 된다) dp[2][n]으로 두어 삭제경우를 추가해준다
dp[0][i]=max(dp[0][i-1]+arr[i],arr[i])
dp[1][i]=max(dp[1][i-1]+arr[i],arr[i],dp[0][i-1])
"""

"""
Tip
어떤 조건을 했는지 안했는지 유뮤는 dp[2][n]으로 해결
방향이 4개거나 갯수라면 dp[4][n] or dp[M][n]으로 해결
"""