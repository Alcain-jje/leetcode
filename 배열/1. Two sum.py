"""
# 1번 완전탐색 풀이법 (5087ms)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        li=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    li.append(i); li.append(j)
                    return sorted(li)
                    #return [i,j]
sol=Solution()
nums=[3,2,4]
target=6
print(sol.twoSum(nums,target))
"""

"""
# 2번 in을 활용한 풀이 (1127ms)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,n in enumerate(nums):
            complement=target-n
            if complement in nums[i+1:]:
                return [nums.index(n),nums[i+1:].index(complement)+i+1]

sol=Solution()
nums=[3,4,4,4,3]
target=6
print(sol.twoSum(nums,target))

"""

"""
# 3번 딕셔너리 활용 (71ms)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map={}
        for i,num in enumerate(nums):
            nums_map[num]=i
        ss=0
        for i,num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return [i,nums_map[target-num],ss]

sol=Solution()
nums=[3,3]
target=6
print(sol.twoSum(nums,target))
"""

"""
# 조회 구조 개선 (63ms) -> 간결해진 코드

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map={}
        for i,num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num]=i
sol=Solution()
nums=[3,3]
target=6
print(sol.twoSum(nums,target))
"""

"""
# 투 포인터 (틀린 풀이)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l=0
        r=0
        num=sorted(nums)
        left, right = 0 ,len(nums)-1
        while left == right:
            if num[left] + num[right] <target:
                left+=1
            elif num[left] + num[right] > target:
                right-=1
            elif num[left] + num[right] == target:
                l = num[left]
                r = num[right]
                break
                
        print(l,r)
        return [nums.index(l),nums.index(r)]

sol=Solution()
nums=[2,7,11,15]
target=9
print(sol.twoSum(nums,target))"""

class Solution(object):
	def twoSum(self, nums, target):
		buffer_dictionary = {}
		for i in range(len(nums)):
			if nums[i] in buffer_dictionary:
				return [buffer_dictionary[nums[i]], i]

			else: # else is entirely optional
				buffer_dictionary[target - nums[i]] = i

sol=Solution()
nums=[2,7,11,15]
target=9
print(sol.twoSum(nums,target))