class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
    
        val1,val2 = edges[0][0],edges[0][1]
        if val1 in edges[1]:
            return val1
        return val2
