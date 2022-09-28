from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for i in wordDict:
            s=s.replace(i,"")
        if not s:
            return True
        else:
            return False


s = "catsandog"
wordDict =  ["cats","dog","sand","and","cat"]
sol=Solution()
print(sol.wordBreak(s,wordDict))