class Node:
    def __init__(self):
        self.children = {}  # Using a dictionary instead of an array
        self.cnt =0
    
    def contains(self, l1,l2):
        return (l1,l2) in self.children
    
    def put(self, l1,l2, node):
        self.children[(l1,l2)] = node
    
    def get(self, l1,l2):
        return self.children.get((l1,l2))
    
  
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word) -> None:
        temp = self.root
        for (c1,c2) in zip(word,reversed(word)):
            if not temp.contains(c1,c2):
                temp.put(c1,c2, Node())
            temp = temp.get(c1,c2)   
            temp.cnt+=1

    def count(self, word: str) -> bool:
        temp = self.root
        m  = len(word)
        i,j = 0 ,m-1
        while(i<m):
            if not temp.contains(word[i],word[j]):
                return 0
            temp = temp.get(word[i],word[j])  
            i+=1
            j-=1  
        return temp.cnt 

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
        trie = Trie()
        for word in reversed(words):
            #for how many word, word[j], this word , word[i]
            #is a prefix of
            ans+=trie.count(word)
            trie.insert(word)
        return ans
        
    
     
