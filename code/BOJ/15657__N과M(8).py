N,M=map(int,input().split(' '))
arrList=list(map(int,input().split(' ')))
arrList.sort()
result=[]
def dfs(idx,cnt):
    if cnt==M:
        print(*result)
        return

    for i in range(idx,N):
        result.append(arrList[i])
        dfs(i,cnt+1) #첫번째 인자 idx가 아니라 i임 주의
        result.pop()
dfs(0,0)

"""
중복조합
idx는 조합을 찾아봐야하는 시작인덱스 전달과 같다
조합이었으면 dfs(i+1,cnt+1) 중복조합은 dfs(i,cnt+1)
"""