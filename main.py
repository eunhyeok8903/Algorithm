from sys import stdin
def rotate(n,d):
    global li
    l_v=li[n][2]
    r_v=li[n][6]

    #회전
    if d==1:
        temp=li[n][7]
        for i in range(7):
            li[n][7-i]=li[n][6-i]
        li[n][0]=temp
    elif d==-1:
        temp=li[n][0]
        for i in range(7):
            li[n][i]=li[n][i+1]
        li[n][7]=temp

    #전이
    print(n,d)
    if n!=1 and l_v!=li[n-1][2]:
        rotate(n-1,-d)
    elif n!=4 and r_v!=li[n+1][6]:
        rotate(n+1,-d)

li=[None]*5
for i in range(1,5):
    s=stdin.readline().rstrip()
    li[i]=[int(ch) for ch in s]
n=int(input())
for i in range(n):
    num,dir=map(int,input().split(' '))
    rotate(num,dir)

cnt=0
for i in range(1,5):
    cnt+=li[i][0]*pow(2,i-1)
print(cnt)