N,M= map(int, input().split(' '))
########(check)input으로 문자열 받고 ' '기준으로 split하면 list생성되고 생성된 리스트 기준 int처리(or함수) 적용 N,M= [2,3] 적용됨
board=[]
K=min(N,M)
cnt=0
def solve():
    for _ in range(N):
        board.append(list(map(int,input()))) #################check
    for i in range(K,0,-1):
        if i==1:
            return 1
        cnt=i
        for j in range(0,len(board)-i+1):
            for k in range(0, len(board[0])-i+1):
                if(board[j][k]==board[j][k+i-1]==board[j+i-1][k]==board[j+i-1][k+i-1]):
                    return cnt
result=solve()
print(result*result)
