class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        freq = Counter(arr)
        pos = 1 
        for val in arr:
            if freq[val] ==1:
                if  pos <k:
                    pos+=1
                else:   
                    return val        
        return ""