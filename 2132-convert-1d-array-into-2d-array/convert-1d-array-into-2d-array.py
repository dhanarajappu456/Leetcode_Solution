class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans  = [ ]
        
        if m*n != len(original):
            return [ ]
        
        curr = []
        for num in original:
            curr.append(num)
            if len(curr) == n:
                ans.append(curr.copy())
                curr  = []
                
        return ans 
            