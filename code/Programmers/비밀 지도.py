# def solution(n, arr1, arr2):
#     answer = []
#
#     length=len(arr1)
#     for i in range(length):
#         temp=2**(n-1)
#         li=[]
#         while(temp>=1):
#             print(arr1[i],arr2[i])
#             a=arr1[i]//temp
#             b=arr2[i]//temp
#             # print("--",a,b,"--")
#             if a==0 and b==0:
#                 li.append(" ")
#             else:
#                 li.append("#")
#             arr1[i]=arr1[i]%temp
#             arr2[i]=arr2[i]%temp
#             temp=temp//2
#         s= "".join(li)
#         answer.append(s)
#     # print(answer)
#     return answer
#

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

"""
문제 
https://programmers.co.kr/learn/courses/30/lessons/17681

한변의 길이가 n(1<=n<=16)인 정사각형 배열 arr1,arr2가 있고
각 배열은 '#' or ' ' 으로 채워진다 
arr1,arr2의 원소값을 이진비트로 나타내었을때
둘다 0이면 ' ' , 하나라도 1 이면 '#'이다. 
"""
"""
문제접근
그냥 구현으로 생각하고 풀었다.
다른 사람 풀이는 비트연산을 이용하여 간단하게 푼게 인상적이었다.
"""
"""
bin(9)  // 0b1001
bin(3)  // 0b11110

이거를 활용하려면 2번 인덱스부터 str로 만들고 
rjust(오른쪽 정렬)을 이용하여 01001, 11110으로 만들어 사용해야했다.

a12= str(bin(i|j)[2:]) //bin으로 이진으로 만들고 i,j를 or연산 하고 인덱스 2부터 str로 
a12= a12.rjust(n,'0') 오른쪼 정렬하고 빈칸은 '0'으로 채움
a12.replace('1','#')
a12.replace('0',' ')
"""