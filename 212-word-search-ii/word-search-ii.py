class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        dir_= [(-1,0),(0,1),(1,0),(0,-1)]
        
        
        #visitedCell in the same path not to be visited again
        visited = set()
        res= set()
        
        class Trie:
            def __init__(self):
                self.isEnd =  False
                self.children = {}
                self.totalReferences = 0
                  
            def addWord(self,word):
                
                s  = self
                
                for c in word:
                    if c not in s.children:
                        s.children[c]= Trie()   
                    s.totalReferences+=1
                    s  = s.children[c]
                    
                s.isEnd = True 
                s.totalReferences+=1
            def removeWord(self,word):
                
                s  = self
                for c in word:
                    if c  in s.children:
                        s.totalReferences-=1
                        s  = s.children[c]                
                s.totalReferences-=1 
                s.isEnd = False
                
           

                
        
        
            
        
        
        def outOfBounds(i,j):
            
            if i< 0 or j <0 or j>=len(board[0])or i>=len(board):
                return True
            return False
        
        
        def rec(i,j,node ,currStr):
            
            if outOfBounds(i,j) or (i,j) in visited or (board[i][j] not in node.children) or node.children[board[i][j]].totalReferences<1:
                return
           
            node = node.children[board[i][j]]
            
            if (node.isEnd==True):
                res.add(currStr+board[i][j])
                root.removeWord(currStr+board[i][j])
           
            visited.add((i,j))
            for d in dir_:
                rec(i+d[0],j+d[1],node,currStr+board[i][j]) 
            visited.remove((i,j))
        
        root =  Trie()
        for word in words:
            root.addWord(word)
      
        for i in range(len(board)):
                for j in range(len(board[0])):
                    rec(i,j,root,"")
        return list(res)
    
            
        