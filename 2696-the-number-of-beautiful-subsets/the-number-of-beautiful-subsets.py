class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        chosen = defaultdict(int)
        nums.sort()

        def rec(i):
          
            if i  == n:
                
                if len(chosen)>0:
                    return 1
                return  0
            tk,not_tk = 0,0 
            if (nums[i]-k) not in chosen:
                chosen[nums[i]]+=1
                tk = rec(i+1)

                chosen[nums[i]]-=1
                if  chosen[nums[i]] == 0:
                    chosen.pop(nums[i])
            not_tk = rec(i+1)
            return not_tk +tk 
                
        return rec(0)

        