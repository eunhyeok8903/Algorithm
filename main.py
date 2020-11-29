from collections import deque
n,m=map(int,input().split(' '))
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dr=[0,0,1,-1]
dc=[1,-1,0,0]
visited=[[False]*m for _ in range(n)]
result=999999

def bfs():
    q=deque()
    q.append((0,0,1))
    visited[0][0]=True

    while q:
        r,c,cnt=q.popleft()
        print(r,c,cnt)
        global result
        if r==n-1 and c==m-1 :
            result=min(result,cnt)
            return result
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]

            if nr>=0 and nc>=0 and nr<n and nc<m:
                if visited[nr][nc]==False and graph[nr][nc]==1:
                    visited[nr][nc]=True
                    q.append((nr,nc,cnt+1))
bfs()
print(result)