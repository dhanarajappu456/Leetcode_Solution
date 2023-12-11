

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        mp = dict()
        n = len(arr)
        arr.sort()
        j=0
        while(j<len(arr)):
            i = j
            while(i+1<n and arr[i]==arr[i+1]):
                i+=1
            
            count   = i-j+1
            if( count/n) > 0.25:
                return arr[i]
            j=i+1
        

        