from collections import Counter 

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        chosen = defaultdict(int)
        nums.sort()
        grps = []
        vis =set()
        num_cnt  = Counter(nums)
        for i , num in enumerate(nums): 
            g={}
            if num not in vis:
                g[num] = num_cnt[num]
                vis.add(num)

                while(num+k in num_cnt):
                    g[num+k] = num_cnt[num+k]

                    vis.add(num+k)
                    num+= k
                grps.append(g)

        def rec(num,grp):
            if num not in grp:
                return 1
            cnt  = num_cnt[num]
            tk  = (2**cnt-1) * rec(num+k+k,grp)
            not_tk = rec(num+k,grp)
            return tk + not_tk
        ans  = 1 
        print(grps)
        for grp in grps:
            min_val = min(grp.keys())
            ans*=rec(min_val,grp)
        return ans-1
            

       

        