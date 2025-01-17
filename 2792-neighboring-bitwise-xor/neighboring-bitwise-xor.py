class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        n   = len(derived)
        initial = 0 
        current = 0
        for i in range(n):
            current = derived[i] ^ current    
        return initial == current