class Trie:

    def __init__(self):
        self.dic={}
    def insert(self, word: str) -> None:
        self.dic[word]=1

    def search(self, word: str) -> bool:
        if word in self.dic:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for i in prefix:
            if i in self.dic:
                return True
            else:
                return False

