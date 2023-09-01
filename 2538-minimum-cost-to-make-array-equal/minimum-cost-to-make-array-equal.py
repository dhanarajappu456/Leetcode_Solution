from sortedcontainers  import SortedDict as dict


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        


        

        #nums_cost = list(zip(nums, cost))
        val_cost_map = dict(int)

        for i in range(len(nums)) :
            val_cost_map[nums[i]] = val_cost_map.get(nums[i],0) + cost[i]
        n =len(val_cost_map)

        pref_cost = [0 for i  in range(n)]
        suff_cost = [0 for i  in range(n)]
        sum_cost = 0
        new_nums  = []
        for val in val_cost_map:
            new_nums.append(val)

        #p#rint(new_nums,val_cost_map)
       
        sum_cost  = val_cost_map[new_nums[0]]
        for i in range(1, n):
            num = new_nums[i]
            gap = new_nums[i] - new_nums[i-1]
            #print(gap,sum_cost)
            pref_cost[i] = pref_cost[i-1] +  gap*(sum_cost)
            sum_cost  +=  val_cost_map[num]
        sum_cost  = val_cost_map[new_nums[-1]]
        for j in range(n-2,-1,-1):
            num = new_nums[j]
            gap = new_nums[j+1] - new_nums[j]
            suff_cost[j] = suff_cost[j+1] +  gap*(sum_cost)
            sum_cost  +=  val_cost_map[num]
        
        ans = float("inf")
        for i in range(n):
            ans = min( ans , pref_cost[i] + suff_cost[i])
        return ans


        #print(pref_cost, suff_cost)
    
        


