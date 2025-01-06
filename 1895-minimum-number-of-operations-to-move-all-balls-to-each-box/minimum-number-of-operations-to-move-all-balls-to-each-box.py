class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        res = [0 for i in range(n)]
        for i  in range(n):
            for j in range(n):
                if j!=i and boxes[j] =="1":
                    res[i]+= abs(i-j)
        return (res)