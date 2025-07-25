class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        pos = 0 
        pos_present = False
        max_neg = -float("inf")
        for num in nums:
            if num>=0:
                pos_present = True
                if num not in s:
                    s.add(num)
                    pos+= num  
            if num<0:
                max_neg  = max(max_neg, num)
                
        return pos if pos_present  else max_neg
            