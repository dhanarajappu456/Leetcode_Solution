class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)
        li = list(d.items())
        li.sort(key = lambda x: x[1])

        arr = li[-k:]
        ans  = []
        for a,b in arr:
            ans.append(a)
        return ans