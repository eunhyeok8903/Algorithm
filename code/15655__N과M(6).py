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
        dfs(i+1,cnt+1)
        result.pop() #  1,2 했던것 빼고 for문돌면 3을 append해서 1,3할 수 있게해야함
dfs(0,0)

"""
조합문제

"""