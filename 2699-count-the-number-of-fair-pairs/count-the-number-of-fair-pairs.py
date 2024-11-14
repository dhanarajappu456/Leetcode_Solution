class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n  = len(nums)
        i,j  = 0, n-1 
        ans  =  0 
        # arr =[i for i in range(n)]
        # arr.sort(key  = lambda x:nums[x])
        # print(arr)
        nums.sort()
        print(nums)
        def low(num  , l,r):
       
            while(l<=r): 
                m = (l+r)//2
               
                if (nums[m] + num)>= lower:
                    r= m - 1
                else:
                    l  = m + 1 
            if  l<n and  (lower<=(num+ nums[l]) <=upper):
                return l
            return -1

        def up(num, l,r):
           
            while(l<=r): 
               
                m = (l+r)//2

                if (nums[m] + num)<=upper:
                    l= m + 1
                else:
                    r  = m - 1 
            if lower<=(num+ nums[r])<=upper:
                return r
            return -1
            
        ans = 0 
        for i in range(n-1):

            l,r  = i+1, n-1
            num = nums[i]
            a,b  = low(num , l,r),up(num,l,r)
            if a!=-1  and b!=-1: 
                ans+= b-a+1 
        return ans 

        
        