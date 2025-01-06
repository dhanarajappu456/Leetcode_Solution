class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        res = [0 for i in range(n)]
        ans=0
        #number of balls so far
        ball =0
        for i  in range(n):

            if ball :
                ans+= ball
            res[i] = ans
            if boxes[i] == "1":
                ball+=1
        ans=0
        ball =0
        for i  in range(n-1,-1,-1):

            if ball :
                ans+= ball
            res[i] += ans
            if boxes[i] == "1":
                ball+=1
        return (res)