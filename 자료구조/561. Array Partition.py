"""
# 내 풀이 1
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        li.sort()
        ans=0
        for i in range(len(li)//2):
            ans+=min(li.pop(),li.pop())
        return ans

li=[1,4,3,2]
sol=Solution()
print(sol.arrayPairSum(li))"""


"""
# 내 풀이 2
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        li = nums
        li.sort()
        ans=0
        plus=0
        for i in range(len(li)//2):
            ans+=min(li[i+plus],li[i+plus])
            plus+=1
        return ans

# 0 1
# 1 2 +1 (2 3)
# 2 3 +2 (4 5)

li=[6,2,6,5,1,2]
sol=Solution()
print(sol.arrayPairSum(li))
"""
"""
# 책 풀이 1
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum=0
        pair=[]
        nums.sort()
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum+=min(pair)
                pair=[]
        return sum
li=[6,2,6,5,1,2]
sol=Solution()
print(sol.arrayPairSum(li))
"""
"""
# 책 풀이 2
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum=0
        nums.sort()
        for n in range(0,len(nums),2):
            sum+=nums[n]
        return sum
li=[6,2,6,5,1,2]
sol=Solution()
print(sol.arrayPairSum(li))

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum=0
        nums.sort()
        for i,n in enumerate(nums):
            if i % 2 == 0:
                sum+=n
        return sum

li=[6,2,6,5,1,2]
sol=Solution()
print(sol.arrayPairSum(li))"""


# 책 풀이 3

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])

li=[6,2,6,5,1,2]
sol=Solution()
print(sol.arrayPairSum(li))
