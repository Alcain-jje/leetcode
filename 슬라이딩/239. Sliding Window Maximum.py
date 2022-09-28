"""class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return nums
        li=[]
        for i in range(len(nums)-k+1):
            li.append(max(nums[i:i+k]))
        return li


nums=[1,3,-1,-3,5,3,6,7]
sol=Solution()
print(sol.maxSlidingWindow(nums,3))"""
import collections

import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []

        for i, n in enumerate(nums):
            if i + 1 < k:
                heapq.heappush(pq, (-n, i))
            else:
                heapq.heappush(pq, (-n, i))
                x, idx = self.find_max(pq, i - k + 1)
                res.append(-x)
                heapq.heappush(pq, (x, idx))

        return res

    def find_max(self, pq: List[int], start: int) -> tuple:
        while True:
            x, idx = heapq.heappop(pq)
            if idx >= start:
                return x, idx

nums=[1,8,-1,-3,5,3,6,7]
sol=Solution()
print(sol.maxSlidingWindow(nums,3))

"""class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        results=[]
        window=collections.deque()
        current_max=float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i<k-1:
                continue
            if current_max == float('-inf'):
                current_max=max(window)
            elif v>current_max:
                current_max=v
            results.append(current_max)
            if current_max == window.popleft():
                current_max = float('-inf')

        return results

nums=[1,-1]
sol=Solution()
print(sol.maxSlidingWindow(nums,1))"""
