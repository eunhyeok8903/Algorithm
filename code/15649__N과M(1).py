N,M = map(int, input().split(' '))
arr= [ i for i in range(1,N+1)]
result=[] #현재담은 숫자
visited=[False]*N #visited배열 생성 및 초기화

def dfs(cnt):
    # print(idx, cnt)
    # print(result)
    if cnt == M:
        print(*result)
        return

    for i in range(N):
        if visited[i]==True:
            continue
        visited[i]=True
        result.append(arr[i])
        dfs(cnt+1)
        result.pop()
        visited[i]=False
dfs(0)


#순열문제
"""
-for문으로 1부터 다시 확인하는데 중복은 허용 x이므로 visited로 중복 check하기(중복순열은 vistied없이 1부터N까지 for문)
-permutation은 iter로 반환, 주소값임
-얘넨 sort안하면 다 나오긴하는데 순서가바뀜
"""


"""
라이브러리 이용 순열
"""
# from itertools import permutations,combinations
# N,M=map(int,input().split(' '))
# p=permutations(range(1,N+1),M)
# print(p)
#
# for i in p:
#     print(' '.join(map(str, i)))  # tuple -> str


# a=[1,2,3]
# p=permutations(a,2)  #튜플 반환
# c=combinations(a,2)
# print(list(p)) #튜플 리스트로 만들기