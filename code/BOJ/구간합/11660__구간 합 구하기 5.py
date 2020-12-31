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
"""
문제 
구간 합 시리즈 4를 풀고 5를 풀자

4 3      //N,M (N<=1024, M<=10만,  N은 정사각 행렬의 크기 M은 구간합 묻는 횟수)
1 2 3 4  //행렬
2 3 4 5  //행렬
3 4 5 6  //행렬
4 5 6 7  //행렬
2 2 3 4  //구간합(x1,y1),(x2,y2) 
3 4 3 4  //구간합
1 1 4 4  //구간합
"""

"""
문제 접근
이거도 시간 제한 때문에 dp사용해야함.

하지만 사격형 모양의 구간합을 구한다는 점이 새로웠다.
그래서 사각형 구간합 별로 dp를 저장해주어야했다.
dp[i][j]=li[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
(i,j까지의 사각형 구간합 = 해당 li원소 더하고 왼쪽,위 사각형들 더하기 (단 이때 중첩해서 더해지는 부분 dp[i-1][j-1]을 한번 빼준다)

구간합 구하기
print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
(x2,y2)에다가 안들어가는부분 2개 빼주면 두번빼준부분 한번 더해주기

위 계산처럼 중복하여 계산된부분 다시 더하거나 빼주는거 주의하기
"""