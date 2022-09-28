#리트코드 풀이
#1번
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        #s[:]=s[::-1]
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] =s[len(s)-1-i],s[i]

sol= Solution()
s=["H","a","n","n","a","h"]

#2번

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left,right = 0 , len(s)-1
        while left < right:
            s[left],s[right]= s[right],s[left]
            left+=1
            right-=1
