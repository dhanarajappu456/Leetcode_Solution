class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()

        arr[0]=1
        n = len(arr)
        for i in range(1,n):
            if arr[i] == arr[i-1]:
                continue
            else:
                arr[i]= arr[i-1]+1
        print(arr)
        return max(arr)
        