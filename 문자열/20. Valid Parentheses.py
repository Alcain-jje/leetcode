# 1번
class Solution:
    def isValid(self, s: str) -> bool:
        char = [')', '}', ']']
        dic={")":"(","}":"{","]":"["}
        stack = []
        for i in range(len(s)):
            if s[i] not in char:
                stack.append(s[i])
            elif not stack or dic[s[i]] != stack.pop():
                return False
        if len(stack)==0:
            return True

s='[]'
sol=Solution()
print(sol.isValid(s))

# 2번
class Solution2:
    def isValid(self, s: str) -> bool:
        answer=[]
        dic={")":"(","}":"{","]":"["}
        for i in range(len(s)):
            if s[i] not in dic:
                answer.append(s[i])
            elif not answer or dic[s[i]] != answer.pop():
                return False
        if not answer:
            return True
        #return len(answer) == 0

# 3번

class Solution3:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict:
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return stack == []

# 4번
class Solution4:
    def isValid(self, s):
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]

# 5번
class Solution5:
    def isValid(self, s):
        while len(s) > 0:
            l=len(s)
            s=s.replace('()',"").replace('{}',"").replace('[]',"")
            if l==len(s): return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l=len(s)
            s=s.replace('()',"").replace('{}',"").replace('[]',"")
            print(s)
            if l==len(s): return False
        return True


s="(([{}]))[[]]()"
sol=Solution5()
print(sol.isValid(s))