dic={3:'은혁',2:'진혁',4:'은영',-1:'은혜'}
li=list(dic.items())
print(li)
li.sort()
print(li)
sdic=sorted(dic.items(), key=lambda x:x[1])
print(sdic)