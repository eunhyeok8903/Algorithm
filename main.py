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