N,M=map(int,input().split(' '))
result=[]
def dfs(cnt):
    if cnt==M:
        print(*result)
        return

    for i in range(1,N+1):
        result.append(i)
        dfs(cnt+1)
        result.pop()
dfs(0)


"""
중복 순열

-중복 조합과의 차이는  1,1,2 1,2,1 을 다른것으로 보고 중복조합은 같은것으로본다
"""

