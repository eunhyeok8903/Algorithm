from sys import stdin
from itertools import combinations

N=int(input())
li=[list(map(int,stdin.readline().rstrip().split())) for _ in range(N)]

person=[i for i in range(N)]
c=combinations(person,N//2)
c=list(c)
lenC=len(c)
result=2000000
for k in range(lenC):
    teamA=c[k]
    teamB=c[-k-1]
    cntA=0; cntB=0
    for i in range(N//2):
        for j in range(N//2):
            cntA+= li[teamA[i]][teamA[j]]
            cntB+= li[teamB[i]][teamB[j]]
    result=min(result,abs(cntA-cntB))
print(result)

"""
문제

N  ( 4<=N<=20 N은 짝수)
0 1 2 3 
4 0 5 6
7 1 0 2
3 4 5 0

각 (1,3)행,열은 1번이 3번과 팀이되었을때 스텟 
(3,1)은 3번이 1번과 팀이되었을때 스텟

이렇게 반반 나누었을 때에 양팀간 스텟차이가 최소가 되는 조합을 구하시오
"""

"""
문제 접근

보고 바로 조합생가이 났다.
근데 20C10은 굉장히 큰 수 일줄 알았는데 1000정도밖에 되지 않았다.

그래서 이를 이용하여 문제 해결(PYTHON3로 하면 시간초과가 나고 PYPY로 해야 통과)
"""

"""
문제 풀이

선수조합
person=[i for i in range(N)]
c=combinations(person,N//2)

유용했던 팁은
전체에서 c[i] 조합의 원소들을 빼면 c[-i-1]과 같다는 점이다.
이 점을 이용해서 코드를 간결화할 수 있었다.
기억하고 사용해야겠다.
(조합에 포함되지 않은 것들(전체의 반인 경우만))
"""