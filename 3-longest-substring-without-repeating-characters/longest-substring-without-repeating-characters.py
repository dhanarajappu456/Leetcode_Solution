class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i,j = 0 , 0 
        chars  = set()
        ans =  0 
        while(j<n): 
            c = s[j]
            while(c in chars ):
                left = s[i]
                if left in chars:
                    chars.remove(left)
                i+=1

            chars.add(c)
            ans = max(ans, j-i+1)
            j+=1
        return ans
