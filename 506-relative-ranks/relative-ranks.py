class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:


        sorted_score =[(num,i) for i,num in enumerate(score)]

        sorted_score.sort(reverse = True)
 
        for i in range(len(score)):
            num ,ind = sorted_score[i]
            if i==0:
                score[ind] = "Gold Medal"
            elif i==1:
                score[ind] = "Silver Medal"
            elif i ==2:
                score[ind] = "Bronze Medal"
            else:
                score[ind] =str(i+1)
        return score

            
        