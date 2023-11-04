class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        for pos in right:
            time  =max(time,(n-pos))
        for pos in left:
            time = max(time ,pos )
        return time        
        