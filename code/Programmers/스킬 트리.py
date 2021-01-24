#위상 정렬 풀이

# def solution(skill, skill_trees):
#     answer = 0
#     arr=[ [] for i in range(26)]
#     idxCnt=[0]*26
#
#     l=len(skill)
#     for i in range(1,l):
#         c1=skill[i-1]
#         c2=skill[i]
#         arr[ord(c1)-65].append(ord(c2)-65)
#         idxCnt[ord(c2)-65]=1
#
#     l=len(skill_trees)
#     for i in range(l):
#         flag=True
#         temp=idxCnt[:]
#         for ch in skill_trees[i]:
#             n=ord(ch)-65
#             if temp[n]==0:
#                 if arr[n]:
#                     temp[arr[n][0]]=0
#                 continue
#             flag=False
#             break
#
#         if flag==True:
#             answer+=1
#
#
#     return answer

# 스택? 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        sk = list(skill)
        flag = True
        for s in skills:
            if s not in sk:
                continue

            if s != sk.pop(0):
                flag = False
                break

        if flag == True:
            answer += 1

    return answer

"""
문제
선행 스킬을 배우고 난 후에 다음에 배울 수 있는 스킬이 정해져있다.

skill  //스킬 트리 순서
"CBD"  

skill_trees // 가능한지 확인해야할 스킬트리들
"""

"""
문제 접근
두가지 방법 다 생각났지만, 위상정렬로 풀어보고 싶었다.
시간 초과가 부담되는 n이 아니여서 당연히 리스트를 이용하는게 깔끔했다.
"""

"""
문제 풀이

skill을 리스트로 나타내고 skill_trees의에서 하나의 스킬트리 검사할때
skill리스트에 해당되지 않으면 그대로 continue하고 
해당되면 리스트의 [0]번 과 다르면 flat==False
같으면 해당 리스트 pop 

어차피 pop의 갯수는 적거나 같기때문에 빈리스트인지 확인할 필요는 없다.

"""