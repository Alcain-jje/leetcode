import collections
class MyHashMap:
    def __init__(self):
        #self.dic=collections.defaultdict(int)
        self.dic={}
    def put(self, key: int, value: int) -> None:
        self.dic[key]=value
    def get(self, key: int) -> int:
        if key in self.dic:
            return self.dic[key]
        else: return -1
        #return self.dic.get(key,-1)
    def remove(self, key: int) -> None:
        if key in self.dic:
            del self.dic[key]

my=MyHashMap()
my.put(15,6)
my.put(4,13)
my.put(6,15)
my.put(11,0)
print(my.get(11))


# 내 풀이
import collections

class MyHashMap:
    def __init__(self):
        self.dic = [-1]*10000001
    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
    def get(self, key: int) -> int:
        return self.dic[key]
    def remove(self, key: int) -> None:
        self.dic[key] = -1
