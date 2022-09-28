# 1번 collections.defaultdict(list) 활용(152ms)
# 딕셔너리에서 list를 value값으로 사용 가능한 라이브러리
"""import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = collections.defaultdict(list)
        li=[]
        for i in strs:
            a[''.join(sorted(i))].append(i)
        for i, j in a.items():
            li.append(j)
        return li"""
# 2번 d.get 활용 풀이(106ms)
import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

strs = ["eat","tea","tan","ate","nat","bat"]
sol=Solution()
print(sol.groupAnagrams(strs))

# 3번 책 풀이
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams =collections.defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return list(anagrams.values())
