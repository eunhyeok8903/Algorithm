"""내코드"""

# from sys import stdin
# N=int(input())
# pattern=stdin.readline().rstrip()
# idx=pattern.find('*')
# l_s=pattern[:idx]
# r_s=pattern[idx+1:]
# for _ in range(N):
#     s=stdin.readline().rstrip()
#     l_len=len(l_s)
#     r_len=len(r_s)
#     flag=True
#     if r_len+l_len>len(s):
#         flag=False
#         print("NE")
#         continue
#
#     for i in range(l_len):
#         if l_s[i]!=s[i]:
#             flag=False
#     for i in range(1,r_len+1):
#         if r_s[-i]!=s[-i]:
#             flag=False
#
#     if flag:
#         print("DA")
#     else:
#         print("NE")

"""개선한 코드"""
from sys import stdin
N=int(input())
pattern=stdin.readline().rstrip().split('*')
front=pattern[0]
back=pattern[1]
for _ in range(N):
    s=stdin.readline().rstrip()
    if s[:len(front)]==front and s[-len(back):]==back and len(front)+len(back)<=len(s):
        print("DA")
    else:
        print("NE")

"""
파이썬적인 사고가 부족했던 문제다.

*이 하나만 주어진다는점에서 split('*')을 사용할수 있었다는것과
front,back을 이용해서 pattern[0],[1]을 할동받고 이를 이용해 
계산했으면 좋았을것같다.

"""