L,C=map(int,input().split())
li=list(input().split())
li.sort()

from itertools import combinations
c=list(combinations(li,L))
for i in c:
    arr=list(i)
    cnt=0
    for ch in arr:
        if ch=='a' or ch=='e' or ch=='i' or ch=='u' or ch=='o':
            cnt+=1
    if cnt>=1 and L-cnt>=2:
        print(''.join(arr))
    else:
        continue

# from itertools import combinations,permutations
# a=[1,2,3]
# p=permutations(a,2)     //튜플형태 반환
# c=combinations(a,2)
"""
from itertools import combinations,permutations

사전순 조합->정렬후 조합
combinations나 permutations는 튜플형태 반환이라서
c= list(combinations())로 받으면
[(a,b,c), (a,c,b),(b,a,c) ] 이런꼴이다.

for tu in c: 로 
각 튜플을 다시 list로 만들어 사용하던지 a,b,c=tu로 받아서 사용하던지 
"""