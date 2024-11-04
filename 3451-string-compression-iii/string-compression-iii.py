class Solution:
    def compressedString(self, word: str) -> str:
        
        n = len(word)
        j = 0 
      

        ans = ""
        prev_c = word[j]
        prev_cnt   = 0 
        while(j<n):
            if prev_c != word[j]:
                #edge case s= a*9y
                if prev_cnt!=0:
                    ans += str(prev_cnt)
                    ans+= prev_c 
                prev_c = word[j]
                prev_cnt = 1
            else:

                prev_cnt+=1 
                if prev_cnt ==9:
                    ans += str(prev_cnt)
                    ans+= prev_c 
                    prev_cnt = 0

            j+=1
        if prev_cnt!=0:     
            ans += str(prev_cnt) + prev_c
        return ans 

            
            

            
        