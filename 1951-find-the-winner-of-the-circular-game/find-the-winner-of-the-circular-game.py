from collections import deque as dq 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:


        nums = dq([i+1 for i in range(n)])

        while(len(nums)>1):

            for i in range(k-1):
                nums.append(nums.popleft())
     
            nums.popleft()
           
        return nums[0]
        