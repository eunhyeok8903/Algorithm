N,M=map(int,input().split(' '))
result=[]
def dfs(idx,cnt):
    if cnt==M:
        print(*result)
        return

    for i in range(idx,N+1):
        result.append(i)
        dfs(i,cnt+1)
        result.pop()
dfs(1,0)


"""
중복조합

-중복을 허용하지만 1,1,4 와 1,4,1은 같은것으로 취급
"""
