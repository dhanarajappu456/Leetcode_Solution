class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        n  =len(nums)
        m = len(l)
        res  =[True for i in range(m)]
       
        for i in range(m):

            a,b =l[i],r[i]

            numbers = set()
            for num in nums[a:b+1]:
                numbers.add(num)
            k = b-a+1
            common_diff = (max(numbers) - min(numbers)) / (k-1)

            
            current = min(numbers)+common_diff
            canOrganise = True
            k=k-1
            while(k):
                if i ==0:
                        print(common_diff,numbers,current)
                if current not in numbers:
                    
                    res[i] =  False
                    break
                current += common_diff
                k-=1
           
        return res


            