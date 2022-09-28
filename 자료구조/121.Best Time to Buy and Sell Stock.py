# 내 풀이
import sys
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxx=0
        minn=1e9
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                minn=min(minn,prices[i])
                maxx=max(maxx,prices[i+1]-minn)
        return maxx

#prices = [2,4,1]
#prices=[2,1,2,0,1]
prices = [2,4,1,2]
sol=Solution()
print(sol.maxProfit(prices))

# 책 풀이
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit =0
        min_price=sys.maxsize
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit

prices = [2,4,1,2]
sol=Solution()
print(sol.maxProfit(prices))


# 다른 풀이

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_profit=0
        while right <len(prices):
            current= prices[right]-prices[left]
            if prices[left]< prices[right]:
                max_profit=max(max_profit,current)
            else:
                left=right
            right+=1
        return max_profit




