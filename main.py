# def solution(dartResult):
#     length=len(dartResult)
#     li=[]; s=0; e=0
#     for i in range(length):
#         if dartResult[i]=='#' or dartResult[i]=='*':
#             continue
#
#         if dartResult[i]>='A' and dartResult[i]<='Z':
#             if i==length-1:
#                li.append(dartResult[s:i+1])
#             else:
#                 if dartResult[i+1]=='#' or dartResult[i+1]=='*':
#                     e=i+1
#                     li.append(dartResult[s:e+1])
#                 else:
#                     e=i
#                     li.append(dartResult[s:e+1])
#                 s=e+1
#     result=[]
#     for s in li:
#         l=len(s)
#         idx=1
#         if s[idx]=='0':
#             idx=2
#         n=int(s[:idx])
#
#         #배수 처리
#         if s[idx]=='D':
#             n=n**2
#         elif s[idx]=='T':
#             n=n**3
#         result.append(n)
#
#         #옵션 처리
#         if s[-1]=='*':
#             if len(result)==1:
#                 result[-1]*=2
#             else:
#                 result[-1]*=2
#                 result[-2]*=2
#         elif s[-1]=='#':
#             result[-1]*=-1
#     answer=0
#     for s in result:
#         answer+=s
#     return answer

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('\d+[SDT][*#]?')
    # p = re.compile('[\d]+[SDT][*#]?')
    dart = p.findall(dartResult)
    print(dart)
    answer=0
    # for i in range(len(dart)):
    #     if dart[i][2] == '*' and i > 0:
    #         dart[i-1] *= 2
    #     dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    #
    # answer = sum(dart)
    return answer
solution("1S2D*3T#")
"""
문제 
3번 다트를 던진다
1S2D*3T //1S 1점, 2D* 2^2 에 이전꺼 포함 x2 , 3T 3^3점 총 37점
1T2D#3D# //1T 1^3점 , 2D# 2^2해당점수 x(-1) , 3D# 3^2*(-1) 총 -4점 
"""

"""
문제접근

간단한 구현문제다.
파싱을 어떻게 할지가 중요한데, 표현식을 이용한 파싱을 생각했지만
문법이 익숙하지 않아서 for문으로 풀어 비효율적이었다.
"""

"""
문제 풀이

for문으로 풀경우 코드가 직관적이지도 않고 실수할 확률이 높아졌다.

정규표현식 문법
https://wikidocs.net/4308

p = re.compile('(\d+)([SDT])([*#]?)')
\d는 숫자와 매치 [0-9] 의미, +는 최소 한번이상 반복 의미
[SDT] S,D,T 중에서 나온다
[*#]?  *,#이 나올수도 있고 안나올수도 있다.
"""