class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = [ (num ,i) for i,num in enumerate(nums)]
        def helper(x):
            x,i = x
            s=  str(x)
            res= ""
            for c in s:
                res+= str(mapping[int(c)])
            return (int(res),i,)
        arr.sort(key=lambda x : helper(x))
        nums =[num for num,i  in arr]
        return nums