N,M=map(int,input().split(' '))
arr=map(int,input().split(' '))
arr=list(arr)
arr.sort()
result=[0 for _ in range(M)]
visited=[False for _ in range(N)]

def dfs(cnt):
    if cnt==M:
        print(*result)
        return

    for i in range(N):
        #print('temp: ',temp)
        if visited[i]==True:
            continue
        visited[i]=True
        result[cnt]=arr[i]
        dfs(cnt+1)
        visited[i]=False

dfs(0,0)

"""
순열 문제
해당 cnt 인덱스에 0부터N-1인덱스를 모두 넣어보며 dfs
"""