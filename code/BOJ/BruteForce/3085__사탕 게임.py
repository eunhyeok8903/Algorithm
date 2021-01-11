from sys import stdin

def countRow(n): #행기준 붙어있는 사탕 카운트
    ch='a'
    cnt=1
    result=1
    for c in li[n]:
        if c==ch:
            cnt+=1
            result=max(result,cnt)
        else:
            cnt=1
        ch=c
    return result

def countCol(n): #열기준 붙어있는 사탕 카운트
    ch='a'
    cnt=1
    result=1
    for i in range(N):
        if li[i][n]==ch:
            cnt+=1
            result=max(result,cnt)
        else:
            cnt=1
        ch=li[i][n]
    return result

def solve(): # 인접한 사탕 바꾸며 세어보기
    #전체 미리 세두기(그래야 나중에 바꾼 열,행에대해서만 카운트 할 수 있음)
    result=0
    for i in range(N):
        vc=countCol(i)
        vr=countRow(i)
        result=max(vc,vr,result)

    # 좌우 바꾸기
    for i in range(N):
        for j in range(N-1):
            li[i][j],li[i][j+1]=li[i][j+1],li[i][j]
            v1=countCol(j)
            v2=countCol(j+1)
            v3=countRow(i)
            result=max(result,v1,v2,v3)
            li[i][j], li[i][j + 1] = li[i][j + 1], li[i][j]

    # 위아래 바꾸기
    for i in range(N-1):
        for j in range(N):
            li[i][j],li[i+1][j]=li[i+1][j],li[i][j]
            v1=countCol(j)
            v2=countRow(i)
            v3=countRow(i+1)
            result=max(result,v1,v2,v3)
            li[i][j],li[i+1][j]=li[i+1][j],li[i][j]

    return result
N=int(input())

li=[list(stdin.readline().rstrip()) for _ in range(N)]
print(solve())

"""
문제 
N주어지고  3<=N<=50
N*N문자열 행렬 주어진다(사탕 색깔)
https://www.acmicpc.net/problem/3085
"""

"""
문제 접근
편하게 풀이할 수 있는 알고리즘을 생각하기전에

브루트 하게 생각해보았다
사탕을 바꿀 수 있는 경우의수가 대략 2500+2500(좌우 바꿀때, 위아래 바꿀때가 있다)
바꿧을때 모든 행열의 최대 값을 구하는 것도 2500+2500 이다.
그럼 5000*5000으로 25000000이고 충분히 시간을 통과할 수 있다.

하지만 난 시간을 더 줄이기 위해서 
미리 행,열의 최대값을 다 계산해두고 바꾸는 행,열만 계산해주었더니 시간이 1/30 으로 줄었다.

다른 알고리즘은 생각해도 생각이 나지 않았고 브루트 포스가 유일한 방법이었다.

"""

"""
문제
1. countRow,conutCol 함수를 만들어 주어진 행,열의 최대값 세어주느 함수 만듦
2. solve를 통해 미리 행열 최대값을 다 세고, 위치 바꾸는 모든 경우를 따져주어 카운팅 해주었다.

TIP
1.swap하는 방법
li[i][j],li[i][j+1]=li[i][j+1],li[i][j]
2.max는 인자갯수 상관없다
"""