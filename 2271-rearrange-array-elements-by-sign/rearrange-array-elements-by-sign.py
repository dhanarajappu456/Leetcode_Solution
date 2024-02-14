class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos,neg = [],[]

        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        res= []
        n= len(nums)
        for i in range(n):
            if i%2==0:
                res.append(pos[i//2])
            else:
                res.append(neg[i//2])
        return res