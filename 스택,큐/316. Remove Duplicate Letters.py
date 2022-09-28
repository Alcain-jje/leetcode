import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix=s[s.index(char):]
            if set(s) == set(suffix):
                return char+self.removeDuplicateLetters(suffix.replace(char,""))
        return ''


#스택과 set을 활용한 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter,seen,stack=collections.Counter(s),set(),[]

        for char in s:
            counter[char]-=1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)

"""# 스택만 사용한 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter,stack=collections.Counter(s),[]
        for char in s:
            counter[char]-=1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                stack.pop()
            stack.append(char)

        return "".join(stack)"""

s="cbacdcbc"
sol=Solution()
print(sol.removeDuplicateLetters(s))