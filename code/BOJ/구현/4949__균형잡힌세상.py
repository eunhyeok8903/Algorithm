while(1):
    s=input()
    stack=[]
    if s==".":
        break

    for i in range(len(s)):
        if s[i]=='.':
            if (len(stack))!=0:
                print('no')
            else:
                print('yes')
            break

        if s[i]=='(' or s[i]=='[':
            stack.append(s[i])
        elif s[i]==')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif s[i]==']':
            if not stack or stack.pop() != '[':
                print('no')
                break

"""
stack으로 list를 이용한점
append 와 pop 
pop하면 마지막 원소 삭제와 동시에 리턴도함
pop했을때 빈리스트면 에러

그래서 if문에 not stack먼저 확인해주어야함

not은 list가 empty인지 확인

"""