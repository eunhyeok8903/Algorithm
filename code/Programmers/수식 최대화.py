import re
from itertools import permutations
def cal(n1, n2, ex):
    if ex=='*':
        return n1*n2
    if ex=='+':
        return n1+n2
    if ex=='-':
        return n1-n2

def solution(expression):
    answer = 0
    p=re.compile('[-+*]')
    temp1=p.findall(expression)
    p=re.compile('[\d]+')
    temp2=list(map(int,p.findall(expression)))

    li=[]
    if '+' in temp1: li.append('+')
    if '-' in temp1: li.append('-')
    if '*' in temp1: li.append('*')
    li.sort()
    ex=permutations(li,len(li))
    for e in ex: #순열 for문
        v=temp2[:]
        c=temp1[:]
        for e_ in e: #우선순위대로 연산 for문
            while len(v)>0 and (e_ in c): #계산
                idx= c.index(e_)
                del c[idx]
                cal_value=cal(v[idx],v[idx+1],e_)
                v[idx]=cal_value; del v[idx+1]
        answer=max(abs(v[0]),answer)
    return answer

# solution("100-200*300-500+20")
solution("50*6-3*2")

"""
문제
https://programmers.co.kr/learn/courses/30/lessons/67257

연산자 우선순위에 따라서 값이 달라진다. 이때 최대가 되는 값을 구하라 
100-200*300-500+20 // *>+>- 로 했을때 -60420 이고 절대값을 씌우면 최대값이 된다.
"""
"""
문제 접근
1.연산자 우선순위를 순열로 완전탐색을 해봐야 한다 생각했고.
2. 그 순위에 따라서 연산을 직접 해보아야 했다. -> 파싱
"""
"""
문제 풀이

1.
#for문으로 나누어도되지만 파이썬 장점인 정규표현식을 사용해서 파싱했다.
    p=re.compile('[-+*]')
    temp1=p.findall(expression)
    p=re.compile('[\d]+')
    temp2=list(map(int,p.findall(expression)))

2.permutation 으로 순열 리스트 만들어준다.
(이때 오륾차순 정렬된 리스트를 인자로 넣어야하고,list로 만들어주는거 습관화하기)

3.연산
list의 내장함수 del과 index를 이용하여 제거해준다.
for문을 돌려서 제거하면 for문이 돌아가는 와중에 인덱스가 꼬일 수 있으므로 while사용 생각하자. 
"""