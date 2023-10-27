class Node : 


    def __init__(self,):

        self.dic ={ }
        self.isEnd  = False

class WordDictionary:

    def __init__(self):
        
        self.head = Node()
        

    def addWord(self, word: str) -> None:

        temp =self.head

        for c in word:
            if c not in temp.dic:
                temp.dic[c] = Node()
            temp  = temp.dic[c]
        temp.isEnd =True
     
        

    def search(self, word: str) -> bool:
        n =len(word)

        def dfs(node, ind):
            if  ind ==n:
                return node.isEnd
            ch = word[ind]
            if ch==".":

                for c in node.dic:
                    if  dfs(node.dic[c],ind+1):
                        return True
                return False
            
            else:
                if ch not in node.dic:
                    return False
                return dfs(node.dic[ch],ind+1)
        return dfs(self.head, 0)

        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)