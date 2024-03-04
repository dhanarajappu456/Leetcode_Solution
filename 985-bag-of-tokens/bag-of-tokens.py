'''
solution - sort and two pointer(greedy)

We know we get a score of 1 for each token , no matter what order we collect , the coin 
so it is ideal to 

1) perform the face up -  collect all the token  sum of whose value is < current power we have.
2) then we need to increase the  power - by face down , in this case it is ideal to get the token that can give max power 
that is to take a token with max power
note when performing the facedown , we need to have a score of atleast 1, to payoff for the operation.

All in all the token must be sorted with the 2 pointers at each end.

t n 
s 1 
'''
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

           

        