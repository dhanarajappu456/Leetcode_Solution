class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        res = 0
        #keeps track of bad , min ,max index
        bad_index, min_index, max_index = -1,-1,-1
        
        for i, num in enumerate(nums) :
            #bad index is the index of recent value that is not in range[mink,maxk]
            if num<mink or maxk<num:
                bad_index = i
            #update the min index
            if num == mink:
                min_index = i
            #update the max index
            if num == maxk:
                max_index = i
            # this is left most index among indices where recent min and max element  lies
            left_index = min(min_index, max_index)
            #counts the valid subarray
            res += max(0,left_index - bad_index)

        return res