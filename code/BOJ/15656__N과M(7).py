N,M=map(int,input().split(' '))
arrList=list(map(int,input().split(' ')))
arrList.sort()
result=[]
def dfs(cnt):
    if cnt==M:
        print(*result)
        return
    for i in range(N):
        result.append(arrList[i])
        dfs(cnt+1)
        result.pop()
dfs(0)

"""
중복순열
중복이 허용되므로 visited없이 진행하였고, 순열은 cnt만 인자로 전달
"""