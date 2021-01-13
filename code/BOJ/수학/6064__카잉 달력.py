from sys import stdin

T = int(input())


def solve(M, N, x, y):
    if M >= N:  # n1>=n2이도록 할당
        n1 = M
        n2 = N
    else:
        n2 = M
        n1 = N
        x, y = y, x
    gap = n1 - n2
    # print(x,y)
    li = [0]
    for i in range(1, n1 + 1):
        if i <= n2:
            li.append(i)
        else:
            li.append(i % n2)
    # print(li)
    check = [0] * (n1 + 2)
    check[li[x]] = 1
    num = li[x]
    temp = [li[x]]
    while (1):
        num = num + gap
        if num > n2:
            num = num - n2
        if check[num] == 1:
            break
        else:
            check[num] = 1
        temp.append(num)

    if check[y] == 0:
        print(-1)
        return

    # print(x,temp.index(y),n1)
    print(x + temp.index(y) * n1)


for _ in range(T):
    M, N, x, y = map(int, stdin.readline().rstrip().split())
    solve(M, N, x, y)


"""
문제 접근
중국인의 나머지 정리
https://casterian.net/archives/609
https://www.acmicpc.net/board/view/21503
"""

"""
주의점

 i in 리스트: 는 시간복잡도 O(N)임을 확실히 새겨두자.
 원소를 추가하면서 리스트 확인하게되면 O(N^2)나와버림
 
 [0]*n = [0,0,0,,,0]
 
"""