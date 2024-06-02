class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n  = len(s)
        i,j  = 0,n-1
     
        
        while(i<=j):
            temp = s[i]
            s[i] = s[j]
            s[ j] = temp
            
            i+=1
            j-=1
     

        