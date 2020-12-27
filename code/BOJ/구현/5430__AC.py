from sys import stdin
from collections import deque

T=int(input())
for _ in range(T):
    func=stdin.readline().rstrip()
    n=int(input())
    s=stdin.readline().rstrip()
    temp_s=s[1:-1]
    if temp_s=="":
        dq=deque([])
    else:
        dq=deque(map(int,temp_s.split(',')))
    flag=False #False면 왼쪽 True면 오른쪽
    check=True
    for f in func:
        if f=='D':
            if not dq:
                check=False
                break
            if flag==False:
                dq.popleft()
            else:
                dq.pop()

        elif f=='R':
            if flag==False:
                flag=True
            else:
                flag=False

    if check==False:
        print('error')
    else:
        if flag==True:
            dq.reverse()

        result=str(list(dq))
        for ch in result:
            if ch==' ':
                continue
            print(ch,end='')
        print()


"""
문자열 처리 엽습에 도움이 되는 구현 문제였다.

다만 시간복잡도를 고려해서 문제를 풀이를 해야했던점이 유의점이다.

R이 나올때마다 reverse해주면 reverse()해줄때마다 O(N)이 소모되기 때문에 flag를 두어 토글해주었고

flag의 상태에 따라서 D가 나올때마다 앞을 삭제할지 뒤를삭제할지를 정해주었다.

앞에 삭제해줄경우 list는 del이나 pop(인덱스)를 이용해주어야하는데 이는 삭제후 원소를 땡겨주므로 O(N)의 시간복잡도 필요하므로

deque를 사용해주었다.
"""