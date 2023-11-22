

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
       
        l,h = 0, nums[-1] - nums[0]

        n  = len(nums)
        def can_be_min_diff(diff):
            i=0
            pairs = 0 
            while(i<n-1):
                #follow greedily , if a num at i  can pair with next one i+1  always pair it , 
                #it is better than pairing the i+1, with next number at i+2 even if its diff is very short
                # not following early index pairing,  cause to  miss some better opportunities
                #eg:
                #p =2 
                #diff=5
                #nums[1 , 3, 4, 5, 20,30 ]
                #if 3 can pair with 1 pair it with 1, don't pair with 4, since doing so makes a pair (4,5) unavialable 
                #and we get 2 pair with that diff cannot be made, but if we had paired (1,3) , then we can pair (4,5 ) which gives 
                #2 pair
                
                if nums[i+1] - nums[i]<= diff:
                    pairs+=1
                    i+=2
                else:

                    i+=1
                
                #check if   p or more  of such number of pairs with difffernce<=diff  can be formed
            return pairs>=p
           


        ans = nums[-1] - nums[0]
        while(l<=h):

            mid = (l+ h)//2
            if can_be_min_diff(mid):
                ans  = mid
                h = mid-1
            else:
                l= mid+1
        return ans

            
        