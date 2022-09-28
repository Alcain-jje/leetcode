import collections

"""# 내 풀이
import collections
class MyStack:
    def __init__(self):
        self.deq=collections.deque()
    def push(self, x: int) -> None:
        self.deq.append(x)
    def pop(self) -> int:
        return self.deq.pop()
    def top(self) -> int:
        return self.deq[-1]
    def empty(self) -> bool:
        if not self.deq:
            return True
        else:
            return False

my=MyStack()
print(my.push(1))
print(my.push(2))
print(my.top())
print(my.pop())
print(my.empty())"""

"""
# 다른 풀이 1
import collections
class MyStack:
    def __init__(self):
        self.deq=collections.deque()
    def push(self, x: int) -> None:
        self.deq.appendleft(x)
    def pop(self) -> int:
        return self.deq.popleft()
    def top(self) -> int:
        return self.deq[0]
    def empty(self) -> bool:
        return len(self.deq) == 0

my=MyStack()
print(my.push(1))
print(my.push(2))
print(my.top())
print(my.pop())
print(my.empty())"""

# 다른 풀이 2
class MyStack:
    def __init__(self):
        self.q=collections.deque()
    def push(self, x: int) -> None:
        self.q.append(x)
        self.q.rotate(1)
        #for i in range(len(self.q)-1):
            #self.q.append(self.q.popleft())
    def pop(self) -> int:
        return self.q.popleft()
    def top(self) -> int:
        return self.q[0]
    def empty(self) -> bool:
        return len(self.q) == 0

my=MyStack()
print(my.push(1))
print(my.push(2))
print(my.top())
print(my.pop())
print(my.empty())