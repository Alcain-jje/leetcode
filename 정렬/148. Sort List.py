"""from typing import Optional
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head != None :
            list1.append(head.val)
            head = head.next
        list1.sort()

        node = dum = ListNode(0)
        for e in list1:
            node.next = ListNode(e)
            node = node.next
        #return dum.next


li=[4,2,1,3]
sol=Solution()
print(sol.sortList(ListNode(li)))"""


"""
#링크드 리스트 구현

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class Linkedlist:
    def __init__(self):
        init=ListNode('init')
        self.head=init
        self.tail=init

        self.current=None
        self.data=0

    def append(self,data):
        new=ListNode(data)
        self.tail.next=new
        self.tail=new
        self.data+=1


l=Linkedlist()
print(l.tail.data)
print(l.tail.next)

print(l.head.data)
print(l.head.next)

l.append(10)
#l.append(20)
#l.append(30)
#l.append(40)
print(l.tail.data)
print(l.tail.next)

print("============")
print(l.head.data)
print(l.head.next)
print(l.head)
print(l.head.next)
print(l.tail.next)
"""


#======================================
#한번 구현 해본 링크드리스트 ->리스트로 변환

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class Linkedlist:
    def __init__(self):
        init = ListNode(0)
        self.head = init
        self.tail = init

        self.current = None
        self.data = 0

    def append(self, data):
        new = ListNode(data)
        self.tail.next = new
        self.tail = new
        self.data += 1

class Solution:
    def sortList(self, head):
        list1 = []
        while head != None :
            list1.append(int(head.data))
            head = head.next
        list1.sort()
        return list1


l=Linkedlist()

l.append(10)
l.append(30)
l.append(50)
l.append(20)
l.append(40)

sol=Solution()
print(sol.sortList(l.head))

