class Solution:
    def maximumSum(self, nums: List[int]) -> int:


        def get_the_sum(s):
            sm = 0 
            while(s):
                sm+= s%10
                s//=10
            return sm
        ans = -1
        mp = defaultdict(int)
        for i,num  in enumerate(nums):
           
            sm = get_the_sum(num)
         
            if sm not in mp:
                mp[sm] = num
            else:
               
                ans =  max(ans, num + mp[sm])
                if mp[sm]<=num:
                    mp[sm] = num
                
        return ans
            
