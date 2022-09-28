"""#dp로 풀이(시간초과 ㅠㅠ)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol1=Solution()
        if s == s[::-1]:
            return s
        else:
            a=s[1:]
            b=s[:len(s)-1]
            return max(sol1.longestPalindrome(a),sol1.longestPalindrome(b),key=len)
s = "ababaccc"
sol=Solution()
print(sol.longestPalindrome(s))"""


"""
#1번 투포인터 활용 (316ms) max 함수 이용
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1
            return s[left+1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""

        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result
"""
"""
#2번 투포인터 활용 (1404ms) 반복문으로 비교하여 큰 값 저장
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1; right += 1
            return s[left+1:right]
        res=""
        for i in range(len(s)):
            tmp=expand(i,i)
            if len(tmp) > len(res):
                res=tmp
            tmp=expand(i,i+1)
            if len(tmp) > len(res):
                res=tmp
        return res

s = "orod"
sol = Solution()
print(sol.longestPalindrome(s))

"""

#DP로 풀기. (7794ms,,)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = True
                    if j-i+1 > len(ans):
                        ans=s[i:j+1]
        return ans

s = "orod"
sol = Solution()
print(sol.longestPalindrome(s))




"""str = "babab"
//i=0
1. i+1:
	expand(0,1) => X

2. i+2:
	expand(0,2) => O
	left=-1
	right=3
	s[0:3] -> bab

//i=1
1. i+1
	expand(1,2) => X
2. i+2
	expand(1,3) => O
	left=0
	right=4
	s[1:4] -> aba

//i=2
1. i+1
	expand(2,3) => X
2. i+2
	expand(2,4) => X

//i=3
1. i+1
	expand(3,4) => X
2. i+2
	expand(3,5) => listIndexError X

max(bab,aba)= bab"""