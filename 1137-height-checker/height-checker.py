class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        cnt =0
        for i,num in enumerate(sorted_height):
            if num!=heights[i]:
                cnt+=1
        return cnt
        