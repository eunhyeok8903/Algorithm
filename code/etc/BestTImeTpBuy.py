def maxProfit(prices):
    size = len(prices)
    dp = [[0] * size for i in range(2)]
    dp[1][0] = prices[0] * (-1)
    print(dp)
    for i in range(1, size):
        print(i)
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i])
        print(dp)
    return max(dp[0][len(prices) - 1], dp[1][len(prices) - 1])

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
문제링크

주식 사고팔기 문제
dp[0][i]=max(dp[1][i-1]+prices[i],dp[0][i-1]) //이번에 판경우, 안사고 그대로 온 경우
dp[1][i]=max(dp[0][i-1]-prices[i],dp[1][i-1]) //이번에 산경우, 안팔고 그대로 온 경우
"""