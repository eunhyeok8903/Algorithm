from sys import stdin
N=int(input())
li=[]
for _ in range(N):
    s,e= map(int,stdin.readline().rstrip().split())
    li.append([s,e])
#회의 끝나는 시간 기준 정렬
li.sort(key=lambda x:(x[1],x[0]))
last_e=-1
cnt=0
for i in range(N):
    s,e=li[i]
    if last_e<=s:
        cnt+=1
        last_e=e
print(cnt)