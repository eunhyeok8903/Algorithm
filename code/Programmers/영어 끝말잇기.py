def solution(n, words):
    answer = []
    l=len(words)
    dic={}; idx=0
    flag=True
    l_word=words[0][0]
    for i in range(l):
        if words[i][0] != l_word: flag=False
        if words[i] in dic: flag=False

        if flag==False:
            idx=i
            break

        dic[words[i]]=1
        l_word=words[i][-1]
    if idx==0:
        answer=[0,0]
    else:
        answer=[(idx%n)+1,(idx+n)//n]



    return answer

"""
문제
https://programmers.co.kr/learn/courses/30/lessons/12981

1.이전 단어의 끝으로 시작해야하고
2.이전에 나온 단어면 안된다
3.두자리 이상 100자리 이하 단어다.
4.모두 이상 없다면 [0,0]반환
"""
"""
문제 접근
이전에 나온단어는 set을 생각했고,
cnt를 만드는것보다 //와 %를 이용하여 계산했다.
"""
"""
문제 풀이
answer=[(idx%n)+1,(idx+n)//n] 

set에서 in 은 O(1)이고
s.add()사용
"""