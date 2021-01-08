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