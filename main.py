from collections import deque
x=3
q=deque([4,5])
tmp=deque([x])
tmp.extend(q)
queue=tmp


print(tmp)

x=10
tmp=deque([x])
tmp.extend(q)
queue=tmp

print(tmp)

