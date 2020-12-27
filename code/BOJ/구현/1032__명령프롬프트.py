from sys import stdin
N=int(input())
s=stdin.readline()
li=list(s)
len=len(s)

for _ in range(1,N):
    temp=stdin.readline()
    for j in range(len):
        if li[j]!=temp[j]:
            li[j]='?'
print(''.join(li))


"""
string은 각요소 값 변경 불가
->list로 바꾸고 다시 string으로 바꾸어야함

s="abcde"
li=list(s)    
print(li)     //['a','b','c','d','e']
temp=''.join(li)    //list를 문자열로 합칠때 각 원소 사이에 어떤값을 넣어서 합칠지 join으로 
print(temp)         //abcde
"""


