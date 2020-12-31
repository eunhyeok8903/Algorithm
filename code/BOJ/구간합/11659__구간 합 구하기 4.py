from sys import stdin
N,M=map(int,stdin.readline().strip().split())
li=list(map(int,stdin.readline().strip().split()))

dp=[0]*(N+1)
for i in range(1,N+1):
    dp[i]=dp[i-1]+li[i-1]
for _ in range(M):
    s,e=map(int,stdin.readline().strip().split())
    print(dp[e]-dp[s-1])

"""
문제
5 3 // N,M
5 4 3 2 1 // N개의 원소들
1 3 // 1부터 3 구간합
2 4 // 2부터 4 구간합
5 5 // 5부터 5 구간합
N<=10만 M<=10만
"""

"""
문제 접근
N,M이 둘다 10만까지 가능해서 
O(N^2)경우 100억이 나온다.

그래서 dp를 생각해봤는데 2차원 dp를 생각해봤는데 2차원 dp를 하게되면 메모리 초과가 이러난다.

결론은 1차원 dp를 이용해야겠다고 생각했고 
2부터 4의 구간합은 (4까지 더한것 - 1까지 더한것)이었다
그래서 dp로 해당 인덱스까지 더한값을 메모이제이션 해두고 

입력받은 s,e를 이용하여 구간합을 구해주었다.
"""
