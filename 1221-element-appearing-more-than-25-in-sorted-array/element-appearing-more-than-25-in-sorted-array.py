

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

      
        n = len(arr)
        for i,num in enumerate(arr):

            if (i+(n//4))<n and arr[i+n//4] == num:
                return num
            