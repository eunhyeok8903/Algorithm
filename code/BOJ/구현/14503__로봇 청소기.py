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
"""
문제
N,M //행 열 크기
r c d // 행렬 좌표(r,c)와 시작방향 d 주어짐 ( 0-북, 1-동, 2-남, 3-서)
행렬 N*M 입력 주어짐 (1은 벽 0 은 청소가능구역)

https://www.acmicpc.net/problem/14503
"""
"""
문제 접근
dfs일거라 생각하여 dfs처럼 접근했지만 
로봇의 이동방식이 dfs이동과는 다르다는것을 코드 구현하면서 알게되었다.

그래서 구현문제의 경우 실제 주어진대로 그려보면서 그대로 일치하게 그려야함을 느꼈다.
"""

"""
풀이 

1. 시작점 출발
2. 주어진 방향대로(바라보고있는 방향 왼쪽부터) 청소가능 구역이 있는지 찾음
3. 있다면 거기로 진입
4. 없다면 뒤로 후퇴(다시 2번부터)

청소하러 이동하면 return 해주는게 중요했다.
또 네방향 모두 없다면
후퇴하는 방향 설정 -> nd=(d+2)%4
nr=r+dr[nd]
nc=c+dc[nd]
dfs(nr,nc,d) // 방향은 그대로 후퇴하므로 넘겨주는건 nd가 아니라 d임이 중요했다.

방향 설정시 TIP
d=(d+3)%4를 하거나 // == d=(d-1+4)%4
dr,dc를 바꾸어서 d=(d+1)%4로 해주기


"""