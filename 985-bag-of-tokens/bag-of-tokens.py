class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort()
        n = len(tokens)
        i,j=0,n-1
        score =0
        ans =0 
        while(i<=j):

            while(i<=j and tokens[i]<=power):
                power-=tokens[i]
                score+=1
                i+=1
                ans = max(ans,score)
            if score>=1:
                power+=tokens[j]
                score-=1
                j-=1
            else:
                break
                
        return ans

           

        