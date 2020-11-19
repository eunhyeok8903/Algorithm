N,M=map(int,input().split(' '))
result=[]
def dfs(idx, cnt):
    if cnt==M:
        print(*result)
        return
    if idx==N+1:
        return

    result.append(idx)
    dfs(idx+1,cnt+1)
    result.pop()
    dfs(idx+1,cnt)
dfs(1,0)

"""
조합 
-#지나온 index 이후부터 dfs진행
"""



"""
라이브러리 사용 
"""
#from itertools import combinations
#c=[1,2,3]
#c=combinations(c,2)
#print(list(c))