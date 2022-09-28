"""class Solution:
    def isValid(self, s: str) -> bool:
        popp={']':'[','}':'{',')':'('}
        check=['(','[','{']
        stack=[]
        for i in s:
            if i in check:
                stack.append(i)
            elif not stack or popp[i]!=stack.pop():
                return False
        return len(stack)==0


# ()), ()(, [)
s="()[]["
sol=Solution()
print(sol.isValid(s))"""


class Solution:
    def isValid(self, s: str) -> bool:
        while len(s)>0:
            l=len(s)
            s=s.replace("()","").replace("{}","").replace("[]","")
            if l==len(s):
                return False
        return True
s="()[][]"
sol=Solution()
print(sol.isValid(s))

"""class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l=len(s)
            s=s.replace('()',"").replace('{}',"").replace('[]',"")
            if l==len(s): return False
        return True"""