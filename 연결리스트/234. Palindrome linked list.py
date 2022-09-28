


"""
# 내 풀이
class Solution:
    def isPalindrome(self, head: list) -> bool:
        l = []
        n = head
        while n is not None:
            l.append(n.val)
            n = n.next
        head = ''.join(map(str, l))
        if head == head[::-1]:
            return True
        else:
            return False

s=[1,2,2,1]
sol=Solution()
print(sol.isPalindrome(s))"""

"""
# 책 리스트 풀이
class Solution:
    def isPalindrome(self, head: list) -> bool:
        q:list = []

        if not head:
            return True
        node=head
        #리스트 변환
        while node is not None:
            q.append(node.val)
            node=node.next
        #펠린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
"""

"""
# 데크 사용 풀이
import collections
class Solution:
    def isPalindrome(self, head: list) -> bool:
        q: list = collections.deque()
        if not head:
            return True
        node=head
        #리스트 변환
        while node is not None:
            q.append(node.val)
            node=node.next
        #펠린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
    """

# 런너 풀이
class Solution:
    def isPalindrome(self, head: list) -> bool:
        rev=None
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            rev,rev.next,slow = slow, rev, slow.next
        if fast:
            slow= slow.next

        while rev and rev.val == slow.val:
            slow, rev= slow.next,rev.next
        return not rev

