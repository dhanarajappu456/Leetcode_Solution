class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for det in details:
            age  = int(det[-4]+det[-3])
            if age>60:
                cnt+=1
        return cnt