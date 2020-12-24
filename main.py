from sys import stdin
S1=stdin.readline().rstrip()
S2=stdin.readline().rstrip()

len1=len(S1)
len2=len(S2)

dp=[[0]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if S1[i-1]==S2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

"""
문자 같을 때
dp[i][j]=dp[i-1][j-1]+1
두글자가 추가되기전 가장 큰 길이에서 +1
AB AC 에서 이미 최고 큰 수가 1로 정해졌으니까 당연히 여기서 +1 된게 ABD ACD에서 최장임

다를 때
이전꺼나 위에꺼에서 가장 큰 수 가져옴


#잔기술
dp[1][1]부터 시작하는 이유는 제일처음 문자가 참조할게 없을때 dp[1][0]참조하게하여 for문안에 dp식으로만 끝나게함
이거안하면 새롭게 조건 달아주거나 따로 또 잔 작업 해줘야함

"""