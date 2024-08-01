class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for det in details:
            
            if (det[-4]>="7")  or (det[-4]=="6" and det[-3]>"0"):
                cnt+=1
        return cnt