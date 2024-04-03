from collections import defaultdict as dict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dir_= [(-1,0),(0,1),(1,0),(0,-1)]
        
        
        #visitedCell in the same path not to be visited again
        visited = set()
        def outOfBounds(i,j):
            
            if i< 0 or j <0 or j>=len(board[0])or i>=len(board):
                return True
            return False
        
        
        def rec(i,j, currCharInd):
            
        
            if outOfBounds(i,j) or (i,j) in visited or   word[currCharInd] != board[i][j]:
                return False
        
           
            
            visited.add((i,j))

            if currCharInd == len(word)-1:
                return True
            for d in dir_:
                if rec(i+d[0],j+d[1],currCharInd+1) ==True:
                    return True
            visited.remove((i,j))
            return False
            
        
        def isAllWordCharCountInBoard():
            
            allCharsBoard = dict(int)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    allCharsBoard[board[i][j]]+=1

            for char in word:

                    if allCharsBoard[char]==0:
                        return False

                    allCharsBoard[char]-=1
            return True
        
        def main():
            #check allChars in word present in board atleast in same quanties
            
            if isAllWordCharCountInBoard()==False :
                return False
            for i in range(len(board)):
                for j in range(len(board[0])):

                    if rec(i,j,0)==True:

                        return True
            return False
        return main()      
        
                
                    
            
             
        
        