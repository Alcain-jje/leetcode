from typing import List

#통과 코드
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans


temperatures = [73,74,75,71,69,72,76,73]
sol=Solution()
print(sol.dailyTemperatures(temperatures))
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li=[]
        for i in range(len(temperatures)):
            big = False
            for j in range(i+1,len(temperatures)):
                #print(temperatures[i],temperatures[j])
                if temperatures[i] < temperatures[j] and not big:
                    li.append(j-i)
                    big=True
            if not big:
                li.append(0)
        return li
"""


"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li=[]
        big=True
        for i in range(len(temperatures)):
            if not big and i>=1:
                li.append(0)
            else:
                big = False
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    li.append(j-i)
                    big=True
                    break

        li.append(0)
        return li"""

"""class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li=[0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                #print(temperatures[i],temperatures[j])
                if temperatures[i] < temperatures[j]:
                    li[i]=j-i
                    break
        return li"""


