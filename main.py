from sys import stdin
def solution():
    global s
    idx=0
    target_idx=0
    for i in range(len-1,0,-1):
        if s[i]>s[i-1]:
            idx=i
            break
    target_idx=idx; target_result=s[idx]
    for i in range(idx,len):
        if s[idx-1]<s[i] and target_result>=s[i]:
            target_idx=i
            target_result=s[i]

    s[idx-1],s[target_idx]=s[target_idx],s[idx-1]
    s=s[:idx]+sorted(s[idx:])
    for ch in s:
        print(ch,end=' ')

N=int(input())
s= map(int,stdin.readline().rstrip().split())
s=list(s)
len=len(s)
if s==sorted(s,reverse=True):
    print(-1)
else:
    solution()

