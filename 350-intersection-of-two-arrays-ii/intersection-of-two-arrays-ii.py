class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1= Counter(nums1)
        ans = []
        for num in nums2:
            if num in nums1:
                ans.append(num)
                nums1[num]-=1
                if nums1[num] == 0:
                    nums1.pop(num)
        return ans 