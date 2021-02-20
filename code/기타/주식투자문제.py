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

"""
다른 풀이 // 그리디 

[7 1 5 3 6 4]라 하면 
이미 주식 가격을 다 알고 있으니 하루간격으로 비교했을 때 오른 값 만큼 sum+= 해주면 된다
continue + 4 + continue + 3 + continue

만약에 다음날 오른다 쳐도

1 3 4 5 이면 1에서 사고 5에 팔아야 제일 좋은건데 
간격 차이를 더해줌으로써 해결가능
2+1+1=4

 
"""