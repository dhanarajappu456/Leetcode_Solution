class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        '''

        fix one parameter age or score in the increading order - (sort it) so that we can apply take  or not take  on other parameter
        

        here we sort it based on age
        then we apply the take  and not take , approac, with (ind, previous-score) as the state

        tabulation of take or not take - instead of prevsCore we take prevind(beacuse index range is known rather than score, so
        that we can crete the dp table)
        '''
        arr = [(ages[i], scores[i]) for i in range(len(scores))]

        #we sort based on age, but remember we might have sama ages , in which case we need to sort them based on the
        #increasing ages
        arr.sort( key = lambda x:(x[0], x[1]))
        n = len(arr)
        dp = [[0 for prev_scoreind in range(n+1)] for ind in range(n+1)]

        for ind in range(n-1, -1, -1):
            #note here we mapped the prev index range form [-1 to n-1 ]to [0 to n]
            for prevScoreInd in range(ind+1):
                tk = 0
                if prevScoreInd == 0 or arr[ind][1] >= arr[prevScoreInd-1][1]:
                    tk = arr[ind][1] + dp[ind+1][ind+1]
                no_take = dp[ind+1][prevScoreInd]
        
                dp[ind][prevScoreInd] = max(tk, no_take)


        return dp[0][0]







        '''

        t n^2
        s n^2 

        '''