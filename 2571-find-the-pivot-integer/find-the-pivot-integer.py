class Solution:
    def pivotInteger(self, n: int) -> int:
        suff= n*(n+1)//2
        pref=0
        for i in range(1,n+1):
            pref+=i
            if pref == suff:
                return i
            suff-=i
        return -1
           