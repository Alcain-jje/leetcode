"""logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
dic={}
for i in logs:
    li=i.split()
    #ans.append(li[0])
    result = ''.join(s for s in li[1:])
    if result.isdigit():
        pass
    else:
        dic[li[0]] = result
sorted_dict = dict(sorted(dic.items(), key = lambda item: item[1]))"""

"""
#logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter=[]
        digit=[]
        for i in logs:
            if i.split()[1].isdigit():
                digit.append(i)
            else:
                letter.append(i)
        l=sorted(letter, key =lambda x:(x.split()[1:],x.split()[0]))
        return l+digit


#logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
sol=Solution()
print(sol.reorderLogFiles(logs))"""


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        res1, res2 = [], []

        for item in logs:
            if item.split()[1].isdigit():
                res2.append(item)
            else:
                res1.append(item.split())

        res1.sort(key=lambda x: (x[1:],x[0]))

        for i in range(len(res1)):
            res1[i] = " ".join(res1[i])
        res1.extend(res2)

        return res1
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol=Solution()
print(sol.reorderLogFiles(logs))



