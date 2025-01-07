class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        final=[]
        for i in words:
            for j in words:
                if i!=j and i in j:
                    
                    final.append(i)
                    break
        return final            
                
        