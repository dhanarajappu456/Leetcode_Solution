from collections import Counter 

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        #sort nums
        nums.sort()
        #keeps dict as the element  , which is a grp , 
        #each grp(dict) contains nums that are adj by a value k  and their count
        grps = []
        #helps to not add the visited item again to the grp, in case of duplicate occurence in the nums

        vis =set()
        #keeps count of each num 
        num_cnt  = Counter(nums)
        #create the grp list ,
        for i , num in enumerate(nums): 
            #each grp to contain num that are adj by value k 
            g={}
            #add th num to grp g ,if num is not  added to
            # grp (happens in case of multiple occurence in nums), already
            #skip
            if num not in vis:
                g[num] = num_cnt[num]
                vis.add(num)
                #adding all adj number that differ by k , to this grp 
                while(num+k in num_cnt):
                    g[num+k] = num_cnt[num+k]

                    vis.add(num+k)
                    num+= k
                #end of current grp , so add it to the grp list
                grps.append(g)
        #like house robber algo, on each grp
        def rec(num,grp):
            #base case , reached end of grp 
            if num not in grp:
                return 1
            #when multiple entry of current number, num
            #then there are 2**cnt-1 non empty subset out of this number , which
            #can be paired with all subset coming from left and right recursion(that is tk and not tak), when
            #taking this number num
            cnt  = num_cnt[num]
            #when taking current number, we cannot take next number in grp, which is at a dist , k
            tk  = (2**cnt-1) * rec(num+k+k,grp)
            not_tk = rec(num+k,grp)
            return tk + not_tk
        ans  = 1 
        #when we have good subset for each grp , multiply them all
        for grp in grps:
            min_val = min(grp.keys())
            ans*=rec(min_val,grp)
        #removing empty set from consideration
        return ans-1
            

       

        