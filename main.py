from collections import deque

dq=deque(maxlen=3)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
dq.append(4)
print(dq)