class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        

        s = set(nums2)

        for num in nums1:
            if num  in s :
                return num
        return -1
