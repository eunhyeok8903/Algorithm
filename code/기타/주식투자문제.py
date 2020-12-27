def maxProfit(prices):
    l = len(prices)
    dp = [[0] * (l + 1), [-2100000000] * (l + 1)]
    print(dp)
    for i in range(1, l + 1):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i-1])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i-1])
    print(dp)
    return (dp[0][-1])

m=maxProfit([7,1,5,3,6,4])
print(m)

"""
XXX기출
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
주식 투자문제

[0]
[1]
로 둬서 dp 사용하는 무제

내가 못푼 이유는
dp 초기값을 어떤걸로 할지 몰라서였다.

[0]은 0으로 초기화 하고 
[1]은 -INF로 초기화 했어야했는데 둘을 나눠서 생각하지 못하고 같은 값으로 초기화 할 생각만 했었다..

"""