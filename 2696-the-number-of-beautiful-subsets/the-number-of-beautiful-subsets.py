class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        chosen = defaultdict(int)
        nums.sort()
        count  = 0 
        def rec(i):
            nonlocal count
            if i  == n:
                #print( chosen)
                if len(chosen)>0:
                    count+=1
                return 
            
            if (nums[i]-k) not in chosen:
                chosen[nums[i]]+=1
                rec(i+1)

                chosen[nums[i]]-=1
                if  chosen[nums[i]] == 0:
                    chosen.pop(nums[i])
            rec(i+1)
                
        rec(0)
        return count
        