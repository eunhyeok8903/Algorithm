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