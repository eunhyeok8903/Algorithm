from sys import stdin

S1=stdin.readline().rstrip()
S2=stdin.readline().rstrip()
len1=len(S1)
len2=len(S2)

dp=[[0]*(len2+1) for _ in range(len1+1)]
sdp=[[""]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if S1[i-1]==S2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            sdp[i][j]=sdp[i-1][j-1]+S1[i-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            if dp[i-1][j]>=dp[i][j-1]:
                sdp[i][j]=sdp[i-1][j]
            else:
                sdp[i][j]=sdp[i][j-1]
print(dp[-1][-1])
print(sdp[-1][-1])

"""
가장긴 문자열이 필요하기때문에 dp에 길이를 저장해줄 뿐만아니라 
그당시 가장 긴 문자열 도 기록해줄 필요가 있다 -> sdp
만약 S1[i]와 S2[i]가 같을 경우 문자열 길이를 하나 증가 시키고 어떤 문자열을 사용할지는 두가지 방법이 있다.
1. sdp[i-1][j]+S1[i](S2[i]도 됨) 
2. sdp[i][j-1]+S1[i]            
두가지 다 최장 수열이 되기 때문에 둘중 아무거나 해도 상관없다

단 구하는 조건이 최장 문자열 1개 구하는 경우일때 가능
코테에서 나왔던거는 가능한 모든 문자열을 구하는 문제가 있었다. 
이경우에는 모든 경우 다 따져주어야 했기때문에 이방식으로는 사용할 수 없고 다른방법 사용해야함
//이부분은 나중에 다시 문제 풀어야함 (BOJ 18892,18837) //KLIS

위에서 푼 방법 이외에도 다른 풀이가 있다.
bottom-up 방식으로 하는 방법이 있는데
dp[-1][-1]에서 dp[i-1][j]와 dp[i][j-1]을 비교하며 올라가는 방식이다. 
dp[i][j]가 dp[i-1][j],dp[i][j-1] 둘보다 클때 대각선으로 올라간다.(이때 dp[i][j]에 해당하는 문자를 기록
그렇지 않다면 dp[i-1][j] 또는 dp[i][j-1] 더 큰쪽으로 이동 
"""