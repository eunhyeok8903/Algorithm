def solution(N, number):
    answer = 0
    s=[set() for i in range(9)]
    for i in range(1,9):
        s[i].add(int(str(N)*i))

    for i in range(2,9):

        for j in range(1,i):
            for a in s[j]:
                for b in s[i-j]:
                    if b==0: continue
                    if a+b>0:
                        s[i].add(a+b)
                    if a-b > 0:
                        s[i].add(a-b)
                    if a*b > 0:
                        s[i].add(a*b)
                    if a//b>0:
                        s[i].add(a//b)
    print(s)
    for i in range(1,9):
        if number in s[i]:
            return i
    return -1

print(solution(5,12))
print(solution(2,11))

"""
문제 
https://programmers.co.kr/learn/courses/30/lessons/42895

5와 사칙연산으로 12를 
12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
이 처럼 표시할 수 있다.

N으로만 표시해서 number의 숫자를 표현할때 N을 최소 몇개사용해야 만들수있는지 결과 return
9이상이면 -1 리턴
"""

"""
문제 풀이
N=5일때
최소값 

1인경우
5

2인경우
55, 5+5, 5-5, 5*5, 5/5 가능

3인 경우
555, 1번나온 경우와 2인경우의 사칙연산 합집합, 2와 1 경우 사칙연산 합집합

...계속 
"""
"""
이전 것을 활용하는 dp특징 캐치 해내는것 뿐만아니라 사칙연산 을통해 만들 수 있느 값이 정해져있다는 것을 알았으면됨

예를들어서

12 = (55+5)/5 인데
(55+5) 는 dp[3]이고 5는 dp[1] 인데

(55+5)에서 dp[3]=dp[2]+dp[1]임을 알 수 있다.
그래서 set을 이용하여 dp들을 구해나가면 된다.
"""