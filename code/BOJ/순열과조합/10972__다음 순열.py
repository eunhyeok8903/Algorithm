from sys import stdin
def solution():
    global s
    idx=0
    target_idx=0
    for i in range(len-1,0,-1):
        if s[i]>s[i-1]:
            idx=i
            break
    target_idx=idx; target_result=s[idx]
    for i in range(idx,len):
        if s[idx-1]<s[i] and target_result>=s[i]:
            target_idx=i
            target_result=s[i]

    s[idx-1],s[target_idx]=s[target_idx],s[idx-1]
    s=s[:idx]+sorted(s[idx:])
    for ch in s:
        print(ch,end=' ')

N=int(input())
s= map(int,stdin.readline().rstrip().split())
s=list(s)
len=len(s)
if s==sorted(s,reverse=True):
    print(-1)
else:
    solution()

"""
문제
N            // 순열의 크기 (1<=N<=10000)
1 2 3 4      // 이 순열 다음에 오는 순열 구해라
"""

"""
문제 접근
itertools의 permutation을 이용하려했는데 N=10000이었다.
그렇게되면 길이 10000인 튜플이 순열의 수만큼 생겨야하는데 메모리초과가 발생한다.

그러므로 순열이 생기는 규칙을 찾고 수학적으로 접근했다.
"""

"""
문제 풀이

1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2 
1 4 2 3
1 4 3 2
이 순서로 진행이 되는데 

규칙은 좌우를 어느 기준으로 나누어 본다 했을때 
오른쪽에서 내림차순이 유지되는 곳까지를 기준으로 좌우를 나눈다 했을때
1 2 4 3 은 1 2 와 4 3 에서 나뉜다
이때 왼쪽기준 가장 오른쪽에 있는 원소는 오른쪽에서 2보다는 크고 2와 가장 가까운 수와 바뀌어야한다.
바뀌고 오른쪽 원소들은 다시 오름차순으로 정렬 해준다. 
"""