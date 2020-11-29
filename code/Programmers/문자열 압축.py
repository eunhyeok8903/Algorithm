def solution(s):
    answer = 9999
    l=len(s)
    if l==1:
        return 1

    for i in range(1,l//2+1):

        cnt=1
        pre=""
        total=0
        for j in range(0,l,i):
            # print("---",i,j,"---")
            # print(pre,s[j:j+i])
            if j+i>l:
                total+=l-j
                break

            if s[j:j+i]==pre:
                if cnt == 1:
                    total+=1
                if cnt==9:
                    total+=1
                if cnt==99:
                    total+=1
                if cnt==999:
                    total+=1
                cnt+=1
            else:
                total+=i
                cnt=1
                pre=s[j:j+i]
        answer=min(answer,total)
    return answer

"""
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
이런식으로 list에 담고 계산 시작해도됨
"""