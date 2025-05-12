class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans  = set()
        digits.sort()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and i!=k    and digits[i] != 0 and digits[k]%2 ==0 :
                        num = digits[i]*100  + digits[j ]*10 + digits[k]
                        ans.add(num)
        return list(sorted(ans))