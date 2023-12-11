

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        mp = dict()
        n = len(arr)
        for num in arr:

            mp[num] = mp.get(num,0)+1

            if mp[num]/n>0.25:
                return num
        


        