"""import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        for i in nums:
            heapq.heappush(heap,(-i))
        for j in range(k-1):
            heapq.heappop(heap)
        return -1*heap[0]



sol=Solution()
nums=[3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums,k))"""


"""class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]"""



"""import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]

sol=Solution()
nums=[3,2,1,5,6,4]
k = 3
print(sol.findKthLargest(nums,k))"""




import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

sol=Solution()
nums=[3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums,k))