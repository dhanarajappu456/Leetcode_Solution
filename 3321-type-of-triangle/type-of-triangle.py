class Solution:
    def triangleType(self, nums: List[int]) -> str:
        arr  = nums
        arr.sort()
        if (arr[0]+arr[1] <= arr[2]  )  or  (arr[0 ]+arr[2]<= arr[1] ) or   (arr[1]+arr[2]<= arr[0]):
            return "none"

        if arr[0] == arr[1] == arr[2]:
            return "equilateral"
        elif arr[0] != arr[1] != arr[2]:
            return "scalene"  
        else:
            return "isosceles"     