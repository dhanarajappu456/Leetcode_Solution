class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        n   = len(derived)
     
        original =[-1 for i in range(n)]
        original[0] = 0
        for i in range(n):
          
            if original[(i+1)%n]==-1:
                original[(i+1)%n] = derived[i] ^ original[i]
            else:
                if original[(i+1)%n] != (derived[i] ^ original[i] ):
                    return False
        return True