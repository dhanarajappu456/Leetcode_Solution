class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        bit  =[ 0 for i in range(n)]
        for i in range(n):
            bit[i] = (bin(nums[i])[2:]).count("1")
       
        arr = nums.copy()
        nums.sort()

        for j in range(n):
            old_ind = nums.index(arr[j])
            prev_cntbit = bit[min(old_ind,j)]
            for k in range(min(old_ind,j),max(old_ind,j)+1):
                if bit[k]!=prev_cntbit:
                    return False
        return True
        
        