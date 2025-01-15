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
    #t:O(m)
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
        #, the idea is trie will contain the key as chars in the left most and right
        #most poistions of a word ,
        #that is char at 
        '''
        1)0, m-1
        2) 1 , m-2
        .
        .
        .

        and so on
        '''

        '''
        also each node containe the cnt variable , that 
        denote the freq of occurence of the particular prefix

        Inside the count function ,  when we check if a words[i] if prefix of any words
        to the right of it  , this cnt variale helps in doing so

        The count function checs if words[i] pref and suff , by 
        comparing the 2 letters in eaach node with
        corresponding  left most and right most characters of itself(words[i])


        '''
        trie = Trie()
        #t:o(n)
        for word in reversed(words):
            #for how many word, word[j], this word , word[i]
            #is a prefix of
            ans+=trie.count(word)
            trie.insert(word)
        return ans
        
    
     
