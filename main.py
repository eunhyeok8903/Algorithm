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

a=9
b=30
print(bin(a))
print(bin(b))
