def solution(s):
    answer = 9999
    l=len(s)
    if l==1:
        return 1

    for i in range(1,l//2+1):

        word=[s[j:j+i] for j in range(0,l,i)]
        print(word)
    return answer
print(solution("aabbaccc"))
