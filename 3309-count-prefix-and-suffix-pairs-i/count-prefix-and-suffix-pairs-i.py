class Node:
    def __init__(self):
        self.children = {}  # Using a dictionary instead of an array
    
    
    def contains(self, letter):
        return letter in self.children
    
    def put(self, letter, node):
        self.children[letter] = node
    
    def get(self, letter):
        return self.children.get(letter)
    
  
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            if not temp.contains(char):
                temp.put(char, Node())
            temp = temp.get(char)    
  
    
    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            if not temp.contains(char):
                return False
            temp = temp.get(char)    
        return True 

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        #startinf from the end of the words list  ,we  make a 
        '''
         pref and suff trie, for the word words[j] and 
        check for all the words words[i] , that comes  before it 
        in the words list ,  if  it could be suff and pref of the 
        word words[j]
        '''
        for j in range(n - 1, 0, -1):
            w = words[j]
            pref_trie = Trie()
            suff_trie = Trie()

            pref_trie.insert(w)
            suff_trie.insert(w[::-1])

            for i in range(j):
                if len(words[i]) <= len(words[j]):
                    pat = words[i]
                    if pref_trie.search(pat) and suff_trie.search(pat[::-1]):
                        ans += 1
        return ans
