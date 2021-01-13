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