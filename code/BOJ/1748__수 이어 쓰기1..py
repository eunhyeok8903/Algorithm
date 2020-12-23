N=int(input())
cnt=0
n=1
while(1):
    if len(str(n))==len(str(N)):
        cnt+=((N-n)+1)*len(str(N))
        break
    else:
        cnt+=9*n*len(str(n))
        n*=10
print(cnt)

"""
각 자리수(한자리수, 두자리 수, 세자리 수)의 개수는 9,90,900,9000,90000씩 늘어난다
"""