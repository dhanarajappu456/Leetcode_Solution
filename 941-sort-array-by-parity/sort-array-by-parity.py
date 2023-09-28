class Solution:
    """

    keep a pointer(i)for pushing in the even numbers at the front and another pointer that iterate(j) on the string as we move 

    kind of technique involved in quicksort

    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:


        n  = len(nums)
        i=0
        for j in range(n):
            #if current number is even push in the number to front , by the positon pointed by the i 
            if nums[j]%2==0:
                temp =nums[i]
                nums[i] = nums[j]
                nums[j]= temp
                i+=1
        return nums


        