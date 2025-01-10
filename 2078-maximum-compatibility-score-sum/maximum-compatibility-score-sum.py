import heapq as h 

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n  = len(students)
        @lru_cache(None)
        def rec(i,ment_taken):
            if i  == n :
                return  0
            max_ = 0
            for j in range(n):
                score = 0
                if( ment_taken & (1<<j)) ==0:
                    for k in range(len(students[i])):
                        if students[i][k] == mentors[j][k]:
                            score +=1 
                    max_ = max(max_, score +rec(i+1, ment_taken | (1<<j)))
            return max_

        return rec(0,0)