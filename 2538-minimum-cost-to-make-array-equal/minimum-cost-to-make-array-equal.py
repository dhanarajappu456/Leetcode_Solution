from sortedcontainers  import SortedDict as dict


#create pref_cost array amd suff_cost array , where the pref_suff[i] indicate the  cost to make all the
#numbers before the num at new_nums[i](in the sorted order) equal to the new_nums[i]

#suff_cost  - > same as above to make all the numbers greater than new_nums[i]  equal to that of the new_nums[ i]#
#at the end calculate the minimum amonf pref_cost#[i] + suff_cost[i]#


#new_num is nothing but to merge all the same ocurrence of same number cost to single number, 
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        #merging the duplicate values cost  - to create the new_nums
        val_cost_map = dict(int)

        for i in range(len(nums)) :
            val_cost_map[nums[i]] = val_cost_map.get(nums[i],0) + cost[i]
        n =len(val_cost_map)


    
        pref_cost = [0 for i  in range(n)]
        suff_cost = [0 for i  in range(n)]
        sum_cost = 0
        new_nums  = []


        #creating the new_nums after merging all the duplicates
        for val in val_cost_map:
            new_nums.append(val)
        #create the pref_cost array 
        sum_cost  = val_cost_map[new_nums[0]]
        for i in range(1, n):
            num = new_nums[i]
            gap = new_nums[i] - new_nums[i-1]
         
            pref_cost[i] = pref_cost[i-1] +  gap*(sum_cost)
            sum_cost  +=  val_cost_map[num]

        #create the suff_cost array
        sum_cost  = val_cost_map[new_nums[-1]]
        for j in range(n-2,-1,-1):
            num = new_nums[j]
            gap = new_nums[j+1] - new_nums[j]
            suff_cost[j] = suff_cost[j+1] +  gap*(sum_cost)
            sum_cost  +=  val_cost_map[num]
        
        #create the minimum of all the possibilities
        ans = float("inf")
        for i in range(n):
            ans = min( ans , pref_cost[i] + suff_cost[i])
        return ans


  
    
        


