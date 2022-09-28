"""import collections
class MyQueue:
    def __init__(self):
        self.deq=collections.deque()
    def push(self, x: int) -> None:
        self.deq.append(x)
    def pop(self) -> int:
        return self.deq.popleft()
    def peek(self) -> int:
        return self.deq[0]
    def empty(self) -> bool:
        if not self.deq:
            return True
        else:
            return False

my=MyQueue()
print(my.push(1))
print(my.push(2))
print(my.peek())
print(my.pop())
print(my.empty())"""


class MyQueue:
    def __init__(self):
        self.list_in=[]
        self.list_pop=[]
    def push(self, x: int) -> None:
        self.list_in.append(x)
    def pop(self) -> int:
        self.peek()
        return self.list_pop.pop()
    def peek(self) -> int:
        if not self.list_pop:
            while self.list_in:
                self.list_pop.append(self.list_in.pop())
        return self.list_pop[-1]
    def empty(self) -> bool:
        if not self.list_in and not self.list_pop:
            return True
        else:
            return False

my=MyQueue()
print(my.push(1))
print(my.push(2))
print(my.peek())
print(my.pop())
print(my.empty())