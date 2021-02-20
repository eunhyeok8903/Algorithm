from collections import deque
def solution(n, edge):
    answer = 0; dq=deque()
    arr=[[] for i in range(n+1)]
    cnt=[0 for i in range(n+1)]
    visited=[ False for i in range(n+1)]
    cntIdx=0


    for i in range(len(edge)):
        a,b=edge[i][0],edge[i][1]
        arr[a].append(b); arr[b].append(a)
    dq.append((1,0))
    visited[1]=True
    idx=0
    while dq: #dq 빌때까지
        a,b=dq.popleft()
        cnt[b]+=1
        for i in range(len(arr[a])):
            val=arr[a][i]
            if visited[val]==True:
                continue
            dq.append((val,b+1))
            visited[val]=True
        idx=b

    return cnt[idx]

"""
문제
https://programmers.co.kr/learn/courses/30/lessons/49189
"""

"""
문제 접근
가장 먼 노드를 구하는것이기 때문에 
cnt를 세며 확장해 나갈수있는 BFS가 생각 났다.
"""

"""
문제 풀이
arr을 nxn 형태로 둘수 있지만 -> pop한 인덱스의 간선을 찾을때 N만큼 소요되기때문에 비효율적 -> vector로 arr만들기

1. 간선 graph 만들기
2. while dq: 를 이용하여 queue에서 하나씩 빼기
3. 뺀값이 visited=True면 넘기고 False면 visited설정 해주고 cnt+=1, 다시 dq에 append
4. 반복
5. 최종 길이의 cnt리턴
"""

"""
개선할 점
1. arr보단 graph로 이름 바꾸기
2. _사용하기
3. [ [] for _ in range() ] 로 vector 나타내기
4. 
while not dq:
while dq:
"""