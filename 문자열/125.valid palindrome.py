"""
#1번
class Solution:
    def isPalindrome(self, x: int) -> bool:
        li = []
        for i in range(len(x)):
            try:
                if x[i].isalnum():
                    li.append(x[i])
                else:
                    pass
            except IndexError:
                pass
        result = ''.join(s for s in li)
        if result == result[::-1]:
            print('true')
        else:
            print('false')

sol=Solution()
a = list(input().lower())
sol.isPalindrome(a)"""
import re

"""
#리트코드 형식 리스트 활용 60ms
class Solution:
    def isPalindrome(self, x: str) -> bool:
        x = list(x.lower())
        li = []
        for i in range(len(x)):
            try:
                if x[i].isalnum():
                    li.append(x[i])
                else:
                    pass
            except IndexError:
                pass
        #리스트 문자열로 변환
        result = ''.join(s for s in li)
        if result == result[::-1]:
            return True
        else:
            return False
"""


#2번 문자열 + 리스트 활용 304ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팬린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

#3번 데크 사용 94ms
import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

#4번 정규표현식 사용 39 ms  

def isPalindrome(self, s: str) -> bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s)

    return s == s[::-1]