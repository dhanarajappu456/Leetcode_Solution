class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans =[]
        def rec(prev):

            if low<=prev<=high:
                ans.append(prev)
            if prev>high:
                return 
            if prev%10<=8:
                rec(prev*10 + prev%10+1)
        for i in range(1,10):
            rec(i)
        ans.sort()
        return ans