from functools import reduce
from collections import deque
"""
# 틀린 풀이
class Solution:
    def multiplyAll(self,s) -> int:
        return eval("*".join([str(n) for n in s]))
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums=deque(nums)
        sol = Solution()
        li=[]
        for i in range(len(nums)):
            a=nums.popleft()
            li.append(sol.multiplyAll(nums))
            nums.append(a)
        return li

nums = [-1,1,0,-3,3]
sol=Solution()
print(sol.productExceptSelf(nums))
"""
"""
# 책 풀이 1
from collections import deque
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out=[]
        p=1
        for i in range(len(nums)):
            out.append(p)
            p=p*nums[i]
        p=1
        for i in range(len(nums)-1,-1,-1):
            out[i]=out[i]*p
            p=p*nums[i]
        return out


nums = [-1,1,0,-3,3]
sol=Solution()
print(sol.productExceptSelf(nums))"""


# 다른 풀이 2
class Solution:
    def productExceptSelf(self, nums):
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre               # prefix product from one end
            pre *= nums[i] # [1*24,1*12,2*4,6*1]
            ans[-1-i]*=suf
            suf*=nums[-1-i]
            print(ans)
        return ans

nums = [1,2,3,4]
sol=Solution()
print(sol.productExceptSelf(nums))
# 1 2 3
# 0 2 3
# 0 1 3
# 0 1 2

# 1 2 3 4
# 0 2 3 4
# 0 1 3 4