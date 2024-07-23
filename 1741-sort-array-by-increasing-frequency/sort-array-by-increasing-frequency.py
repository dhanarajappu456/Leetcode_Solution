class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nm = nums.copy()
        nums.sort(key=lambda x: (nm.count(x),-x))
        return  nums
        