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
# c=permutations(a,2)
