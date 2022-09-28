import bisect
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        nums.sort()
        start=0
        last=len(nums)-1
        while start <= last:
            mid = (start+last)//2
            if nums[mid] == target:
                #return nums.index(target) # o(n)으로 되기 때문에 비효율적
                return mid
            elif nums[mid] > target:
                last = mid-1
            else:
                start= mid+1

        return -1




nums = [-1,0,3,5,9,12]
target = 8
sol=Solution()
print(sol.search(nums,target))



idx = bisect.bisect_left(nums,target)
print(idx)
"""for i in range(len(nums)):
    if nums[i]"""