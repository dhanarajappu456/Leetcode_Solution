class Solution:
    def maxScore(self, s: str) -> int:
        

        tot_zero , tot_ones = s.count('0') , s.count('1')
        score = 0
        l_zero,l_one = 0,0
        n = len(s)
        #since we need left and right to be non empty , we can't have right as empty, 
        #which happens when i ==n-1
        for i in range(n-1):

            if s[i] == '0':
                l_zero+=1
            else:
                l_one+=1

            r_one = tot_ones - l_one
           
            score = max(score, l_zero+r_one)
        return score

            