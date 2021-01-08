from sys import stdin,stdout
dr=[0,1,0,-1]
dc=[1,0,-1,0]
N=int(stdin.readline())
number=int(stdin.readline())
r,c=(N//2)+1,(N//2)+1
arr=[[0]*(N+1) for i in range(N+1)]
arr[r][c]=1

flag=0
cnt=0
dir=0
result_r,result_c=0,0
for i in range(2,N*N+1):
    if r==c and r<=(N//2)+1:
        r-=1
        c-=1
        flag+=2
        dir=0

    r= r+dr[dir]
    c= c+dc[dir]
    arr[r][c]=i
    cnt+=1
    if cnt==flag:
        cnt=0
        dir+=1
    if i==number:
        result_r=r
        result_c=c
for i in range(1,N+1):
    for j in range(1,N+1):
        print(arr[i][j],end=' ')
    print()
print(result_r,result_c)

"""
문제
https://www.acmicpc.net/problem/1913
"""
"""
문제 접근

수학적으로 접근했는데 딱히 규칙이 없었다.
그래서 구현으로 접근하기 시작했다
"""
"""
문제 풀이
시작점을 기준으로 
오른쪽으로 2칸 아래로 2칸 왼쪽으로 2칸 위로 2칸 이동후
오른쪽으로 4칸 아래로 4칸 왼쪽으로 4칸 위로 4칸 이동하는 식으로 규칙적으로 움직임을 알 수 있었고 이를 구현해야했다.

하지만 N,N에서 시작하면 오른쪽으로 갈때만 2n-1칸 이동하기 때문에 이를 구현하기 까다로웠다.

그래서 생각한 방법이 r==N and c==N 일때 r-1 c-1을 해주어서 다른방향과 같이 2n으로 움직일 수 있게 해주었다.
(여기서 주의점은 우측하단 꼭지점에서도 N,N이 된다는 점이다 그래서 조건을 하나 더 넣어주었다.     if r==c and r<=(N//2)+1:  )

"""