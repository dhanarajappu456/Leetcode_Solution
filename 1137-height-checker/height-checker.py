from collections import defaultdict as dict 

#bucket sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = []
        cnt  = dict(int)
        ans = 0 
        for i,num in enumerate(heights):
            cnt[num]+=1
   
        for val in range(1,101):
            count = cnt[val]
            for i in range(count):
                sorted_height.append(val)
        

        for i,val in enumerate(heights):
            if val!= sorted_height[i]:
                ans+=1
        return ans
        


           




        