from collections import defaultdict as dict
'''
idea is simple, 

we traverse the array and for each char as the middle char in the palindrome we see if we can make palindromes where endchar on either side is anyof the 26 letter, to find if the endchar present on either 
side we keep a set which collect all the letter seen previously and 
 a dictionary that keeps the last index of a character 


 t n *26 
 s 26*26 the ans dict size 
 
 (for any charcter as middle charcter at max ,we can have 26
    plaindromes 
    
    for all 26 letter as middle char, we can therefore have 26*26
    palindromes 
   )

'''
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        prev  = set()
        #maps a character  c to set of plaindromes
        # where c is the middle char of each palindrome in the set  
        ans  = dict(set)
        lastIndex = dict(int)

        for i,c in enumerate(s):
            lastIndex[c]= i 


        for i,c in enumerate(s):
            #checks if each character is present on left and right side of the current character as the middle character 
            for endChar in "abcdefghijklmnopqrstuvwxyz":
                if endChar in prev and lastIndex[endChar]>i:
                    ans[c].add(endChar)
            
          
            prev.add(c) 
        
        res =0 
        #find total palindromes got
        for c in ans:
            res += len(ans[c])
        return res 
        
        
        
        
        