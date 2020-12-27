# from sys import stdin
# def rotate(n,d):
#     global li
#     r=[0,0,0,0,0]
#     r[n]=d
#
#     if n==1: #시계방향
#         if li[1][2]!=li[2][6]:
#             r[2]=d*(-1)
#
#         if r[2]!=0:
#             if li[2][2]!=li[3][6]:
#                 r[3]=r[2]*(-1)
#
#         if r[3]!=0:
#             if li[3][2]!=li[4][6]:
#                 r[4]=r[3]*(-1)
#
#     elif n==2:
#         if li[2][6]!=li[1][2]:
#             r[1]=r[2]*(-1)
#
#         if li[2][2]!=li[3][6]:
#             r[3]=r[2]*(-1)
#
#         if r[3]==0:
#             r[4]=0
#         else:
#             if li[3][2]!=li[4][6]:
#                 r[4]=r[3]*(-1)
#     elif n==3:
#         if li[3][6]!=li[2][2]:
#             r[2]=d*(-1)
#
#         if li[3][2]!=li[4][6]:
#             r[4]=d*(-1)
#
#         if r[2]!=0:
#             if li[1][2]!=li[2][6]:
#                 r[1]=r[2]*(-1)
#     else:
#         if li[4][6]!=li[3][2]:
#             r[3]=d*(-1)
#
#         if r[3]!=0:
#             if li[3][6]!=li[2][2]:
#                 r[2]=r[3]*(-1)
#
#         if r[2]!=0:
#             if li[2][6]!=li[1][2]:
#                 r[1]=r[2]*(-1)
#
#     return r
# li=[[0,0,0,0,0,0,0,0]]
# for _ in range(4):
#     temp=stdin.readline().rstrip()
#     arr=[int(ch) for ch in temp]
#     li.append(arr)
# n=int(input())
# for _ in range(n):
#     num,dir=map(int,input().split())
#     result=rotate(num,dir)
#     for i in range(1,5):
#         if result[i]==-1:
#             temp=li[i][0]
#             for j in range(7):
#                 li[i][j]=li[i][j+1]
#             li[i][7]=temp
#         elif result[i]==1:
#             temp=li[i][7]
#             for j in range(7):
#                 li[i][7-j]=li[i][6-j]
#             li[i][0]=temp
# print(li[1][0]+li[2][0]*2+li[3][0]*4+li[4][0]*8)

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


"""
li=[None]*4  //[None,None,None,None]
li=[4]*4     //[4,4,4,4]

첫번째 방법은 
n,d에 맞게 일일히 구현해주었고
두번째 방법은
일일히 구현하는대신 l_v , r_v를 저장해서 주변 톱니를 회전시키는 방법으로 구현했다.

주의해야할점은
회전시 
li[n][i]값을 li[n][i+1]로 옮기는 작업인데
덮어씌워지는 부분부터 시작해야지 그렇지 않으면 같은 값으로 쭉가게됨
ex
->1 2 3 4 5
->1 2 3 4 4
->1 2 3 3 4
->1 2 2 3 4
->1 1 2 3 4

잘못된 ex
->1 2 3 4 5
->1 1 1 1 1
 
 
10101010을
list("10101010")하게되면 
['1','0' ....'0']으로 된다는점

"""