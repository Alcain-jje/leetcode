from typing import List

# 풀이 1 DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j + 1]:
                    print(s[i:j + 1])
                    dp[j + 1] = True
        return dp[-1]

# 풀이 2
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]

s = "catsandog"
wordDict =  ["cats","dog","sand","and","cat"]
sol=Solution()
print(sol.wordBreak(s,wordDict))

