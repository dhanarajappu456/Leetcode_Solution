class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        #making the value at index i such that of form
        # old + new * a constant_value , here the const_val we chose is 5000
        # this way it preserve old value which can be recovered by 
        #nums[nums[i]] % 5000
        # after the transoformation each index  will contain
        # the new value that is supposed to be there
        # which can be returned , by nums[i] // 5000

        #transoformation to the array elements 
        for i in range(n):
            nums[i]  = nums[i] +  (nums[nums[i]] % 5000)*5000
        
        #getting the value at each index, back
        for i in range(n):
            nums[i]  =  nums[i] //5000
        return nums