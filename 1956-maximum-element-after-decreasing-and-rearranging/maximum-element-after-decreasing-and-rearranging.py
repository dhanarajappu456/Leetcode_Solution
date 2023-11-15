# sort the array, 
# make first element as zero as the elements in the array always>=1
# then starting from 1st index, if curr element ==  prev element  leave it as such , else 
# might need to reduce it to a number just 1 greater than prev element(as absof adj element cant be more than 1)

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        ans  =1 
        arr[0]=1
        n = len(arr)
        for i in range(1,n):
            if arr[i] == arr[i-1]:
                continue
            else:
                arr[i]= arr[i-1]+1
            ans  = max(ans, arr[i])

        return ans


    '''
    t n
    s 1

    '''
        