class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        freq_map = Counter(s)
        odd_cnts = 0 
        for cnt in freq_map.values():
            if cnt%2 ==1:
                odd_cnts+=1
        return odd_cnts <= k