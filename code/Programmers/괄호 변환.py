import sys
sys.setrecursionlimit(10**7)

def check(s):
    v=0
    for ch in s:
        if ch==')':
            v-=1
        else:
            v+=1
        if v<0: return False
    return True
def equal(s):
    if s=="":
        return ""
    temp=[]
    for i in range(len(s)):
        if s[i]=='(':
            temp.append(')')
        else:
            temp.append('(')

    return "".join(temp)

def solution(p):
    if check(p)==True:
        return p
    if p=="":
        return p

    answer = ''
    l=0; r=0
    length=len(p)
    u="";v=""
    for i in range(length):
        if p[i]=='(':
            l+=1
        else:
            r+=1
        if l==r:
            u=p[:i+1]; v=p[i+1:]
            break
    if check(u)==True: v=solution(v)
    else:
        vTemp=equal(u[1:-1])
        u='('+solution(v)+')'
        v=vTemp[:]
    answer=u+v
    return answer
"""
문제 
https://programmers.co.kr/learn/courses/30/lessons/60058
"""

"""
문제 접근

구현 문제다.
하지만 본인 생각대로 하려하다가 틀리는 문제다.
주어진대로만 구현하면 큰 문제 없지만 본인생각을 조금만이라도 넣으면 틀릴수 있다.
"""

"""
문제 풀이

알아낸 점
import sys
sys.setrecursionlimit(10**7)
#재귀 제한 뚫어주는 함수

li= temp[1:-1] -1이면 뒤에서 두번째다
끝은 0도 아니고 그냥 공란으로 두어야함
"""

