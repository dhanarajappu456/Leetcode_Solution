

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
       
        l,h = 0, nums[-1] - nums[0]

        n  = len(nums)
        def can_be_min_diff(diff):
            i=1 
            pairs = 0 
            while(i<n):

                contributing_index =set()
                while(i<n and (nums[i]-nums[i-1])<=diff):
                    contributing_index.add(i)
                    contributing_index.add(i-1)
                    i+=1
                    break
                pairs += len(contributing_index)//2
                i+=1
           
            return pairs>=p
            for i in range(1,n):
                if nums[i]- nums[i-1]<=diff:

                    contributing_index.add(i)
                    contributing_index.add(i-1)
            return len(contributing_index)>=2*p



        ans = nums[-1] - nums[0]
        while(l<=h):

            mid = (l+ h)//2
            if can_be_min_diff(mid):
                ans  = mid
                h = mid-1
            else:
                l= mid+1
        return ans

            
        