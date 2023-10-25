class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        '''

        fix one parameter age or score in the increading order - (sort it) so that we can apply take  or not take  on other parameter
        

        here we sort it based on age
        then it becomes the lis problem 

        and the dp[i] stores the max score from 0 to i in the sorted array ending at i(ie, including the score at index i in the arr)
        '''
        arr = [(ages[i], scores[i]) for i in range(len(scores))]

        #we sort based on age, but remember we might have sama ages , in which case we need to sort them based on the
        #increasing score
        arr.sort( key = lambda x:(x[0], x[1]))
        n = len(arr)
        ans = 0
        dp = [ arr[i][1] for i in range(n)]

        for i in range(n):
            j= i-1
            while(j>=0):

                if arr[j][1]<=arr[i][1]:

                    dp[i] = max(dp[i ], arr[i][1]+ dp[j])
                
                j-=1
            ans = max(ans, dp[i])
        return ans

        '''

        t n^2
        s n

        '''