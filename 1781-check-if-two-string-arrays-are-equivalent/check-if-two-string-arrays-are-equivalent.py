'''

2 pass solution 
make the array to string - 1 traversal
then iterate th string to check equality

t mn  m,n = len of array and len of each word
 
s mn 

'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        word1 , word2 = "".join(word1), "".join(word2)
        if word1 == word2:
            return True
        return False

      