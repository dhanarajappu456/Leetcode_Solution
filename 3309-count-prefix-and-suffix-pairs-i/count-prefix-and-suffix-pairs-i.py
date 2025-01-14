class Node:
    def __init__(self):
        self.arr=[None for i in range(26)]
        self.flag=False
    def contains(self,letter):
        return self.arr[ord(letter)-97]!=None    
    def put(self,letter , node):
        self.arr[ord(letter)-97]=node
    def get(self,letter):
        return self.arr[ord(letter)-97]
    def setEnd(self):
        self.flag=True
    def getEnd(self):
        return self.flag==True
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, word: str) -> None:
        temp =self.root
        for i in word :
            if not temp.contains(i):
                temp.put(i,Node())
            temp=temp.get(i)    
        temp.setEnd()    
    def search(self, word: str) -> bool:
        temp =self.root
        for i in word :
            if not temp.contains(i):
                return False
            temp=temp.get(i)    
        return True 
  


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0 
        n   = len(words)
        for  j in range(n-1,0,-1):
            w = words[j]
            pref_trie = Trie()
            suff_trie  = Trie()

            pref_trie.insert(w)
            suff_trie.insert(w[::-1])

            for i in range(j):
                if len(words[i]) <= len(words[j]):
                    pat  = words[i]
                    if pref_trie.search(pat) and suff_trie.search(pat[::-1]):
                        ans+=1
        return ans