class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        class Node:
            def __init__(self):
                self.children = {}
                self.cnt = 0 
            
            def get(self, c):
                if c in self.children:
                    node  = self.children[c]
                    return node
                return False
            def put(self,c):
                self.children[c] = Node()
                return True
        class Trie:

            def __init__(self):
                self.root  = Node()
            
            def insert(self,w):
                node  = self.root
                for c in  w:
                    if c not in node.children:
                        node.put(c) 
                    node = node.get(c)
                    node.cnt+=1
                
            def search(self, w):
                node  = self.root
                for c in  w:
                    if c not in node.children:
                        return (False, 0 )
                    node = node.get(c)
                return (True, node.cnt)           
        cnt = 0
        trie  = Trie()
        for word in words:
            #no need to put all chars in the word, at max len(pref) 
            #number of  chars is need to put
            trie.insert(word[:min(len(word),len(pref))])
        present, cnt = trie.search(pref)
        return cnt