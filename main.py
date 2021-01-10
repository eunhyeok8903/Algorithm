from sys import stdin

def dfs(r,c,d):
    global cnt,dr
    if li[r][c]==0:
        li[r][c]=2
        cnt+=1

    # print(cnt)
    # for i in range(N):
    #     for j in range(M):
    #         print(li[i][j],end=' ')
    #     print()
    # print("\n\n")

    for i in range(4):
        nd=(d+3)%4
        nr=r+dr[nd]
        nc=c+dc[nd]
        if nr>=0 and nc>=0 and nr<N and nc<M and li[nr][nc]==0:
            dfs(nr,nc,nd)
            return
        d=nd

    nd=(d+2)%4
    nr=r+dr[nd]
    nc=c+dc[nd]
    if nr<0 or nc<0 or nr>=N or nc>=M or li[nr][nc]==1:
        return
    dfs(nr,nc,d)

N,M=map(int,input().split())
r,c,d=map(int,input().split())
li=[]
dr=[-1,0,1,0]  # 북 동 남 서
dc=[0,1,0,-1]
cnt=0

for i in range(N):
    temp=list(map(int,stdin.readline().split()))
    li.append(temp)

dfs(r,c,d)
print(cnt)
