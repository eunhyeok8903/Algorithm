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

"""
문제 접근
그리디라고 생각하기는 정말 어려운것같다..
그리디 문제로 알고있어서 풀었던 거지 처음 주어졌으면 몰랐을거다

그리디 문제는 최대한 많이 풀어보고 잘 정리해둬야할듯
"""

"""
풀이

회의가 끝나는 시각을 기준으로 오름차순 정렬하게 되면 

순서대로 회의를 살펴보면
회의의 시작하는 시각이 이전 그리디 하게 끝난 마지막 회의의 끝난시각보다 같거나 이후면 그회의로 결정임 

만약 
이전회의가 [3,5] 이고 다음 회의가 [5,7] 과 [6,7]이 있다고 하자 [5,7]이 다음 회의가 되고 
이 회의이 끝나는 시간을 last_e에 기록해준다.
그러면 6,7은 어차피 끝나는 시간이 5,7과 같으므로 볼필요가 없다 

이런식으로 그릴디하게 최대 회의 시간을 구할 수 있다.  
"""

"""
정렬 방법 checklist에서 참고 정리 암기
"""