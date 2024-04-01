class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        res = 0
        bad_index, min_index, max_index = -1,-1,-1
        
        for i, num in enumerate(nums) :
            if num<mink or maxk<num:
                bad_index = i

            if num == mink:
                min_index = i

            if num == maxk:
                max_index = i
            left_index = min(min_index, max_index)
            print(left_index,bad_index, left_index-bad_index)
            res += max(0,left_index - bad_index)

        return res