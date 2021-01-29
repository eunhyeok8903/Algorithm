from itertools import product
import math
p=[chr(65+i) for i in range(26)]
p=list(product(p,repeat=2))

def solution(str1, str2):
    answer = 0
    str1=str1.upper(); str2=str2.upper()
    l1=len(str1); l2=len(str2)
    dic1={}; dic2={}
    for i in range(l1-1):
        if str1[i]<'A' or str1[i]>'Z' or str1[i+1]<'A' or str1[i+1]>'Z':
            continue

        temp=str1[i:i+2]
        if temp in dic1:
            dic1[temp]+=1
        else:
            dic1[temp]=1

    for i in range(l2-1):
        if str2[i]<'A' or str2[i]>'Z' or str2[i+1]<'A' or str2[i+1]>'Z':
            continue

        temp=str2[i:i+2]
        if temp in dic2:
            dic2[temp]+=1
        else:
            dic2[temp]=1
    union=0
    inter=0
    for s in p:
        temp=s[0]+s[1]
        if temp in dic1 and temp in dic2:
           inter+=min(dic1[temp],dic2[temp])
        v1=0
        v2=0
        if temp in dic1:
            v1=dic1[temp]
        if temp in dic2:
            v2=dic2[temp]
        union+=max(v1,v2)
    if union==0:
        return 65536

    answer= math.floor((inter/union)*65536)

    return answer

solution("FRANCE","french")
solution("aa1+aa2","AAAA12")
solution("handshake","shake hands")
solution("E=M*C^2","e=m*c^2")

"""
문제
https://programmers.co.kr/learn/courses/30/lessons/17677
"""

"""
문제 접근

문자열을 이용한 구현 문제였다.
"""

"""
문제 풀이

내풀이
1.upper를 이용하여 대소문자 통일
2. 알파벳 범위를 이용하여 알파벳 이외 문자 제거
3. dictionary를 이용하여 가각 나오는 단어 카운팅
4. product(중복순열)을 이용하여 'AA'-'ZZ' 구해둠
5. for문을 이용하여 합집합과 교집합 구해냄

다른 풀이
1. re.findall 표현식을 이용하여 해당 리스트에 if not이면 str1, str2리스트에 추가
2. str1,str2를 set함수를 이용하여 만듦
3. &,| 이용하여 확인해야할 교집합 리스트와 합집합 리스트를 만듦
4. 만든 교집합, 합집합 리스트를 for문으로 돌면서 count를 sum 해준다

"""