from typing import List
"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=0
        minn=1e9
        li=[]
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                minn=min(minn,prices[i])
                maxx=max(maxx,prices[i+1]-minn)
            elif prices[i] > prices[i+1]:
                li.append(maxx)
                maxx=0
                minn=1e9
        if not li:
            li.append(maxx)
        return sum(li)"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                result+=prices[i+1]-prices[i]
        return result

prices = [7,1,5,3,6,4]
prices=[6,1,3,2,4,7]
sol=Solution()
print(sol.maxProfit(prices))