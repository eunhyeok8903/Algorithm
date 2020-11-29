N=int(input())
arr=list(map(int, input().split(' ')))
dp=[-1001]*N
dp[0]=arr[0]
result=-1001
result=max(result,dp[0])
for i in range(1,N):
    temp=dp[i-1]+arr[i]
    if temp<arr[i]:
        dp[i]=arr[i]
    else:
        dp[i]=temp
    result=max(result,dp[i])
print(result)

"""
연속 합 최대가 되는 값 찾기
이런 경우는 대부분 brute하게하면 시간 초과가 난다.
알고리즘 이용하여 시간복잡도 줄임 -> DP
10  -4  3  1  5  6  -35  12  21  -1 이경우 해당 인덱스에서 전에것을 연장할지, 새로 시작할지 결정
10  6   9 10 15  21  -14 12  33  32  // 12에서 -14에 이어서 12를 더하는것보다 12부터 새로시작하는게 크므로 

"""