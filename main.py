import copy

li=[[1,2,3],[4,5,6]]
temp=copy.copy(li)
# li=[1,2,3]
# temp=li[:]
li[1][0]=5
# li[1]=5

print(li)
print(temp)