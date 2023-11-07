class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        n = len(dist)
        time =[dist[i]/speed[i] for i in range(n)]
        time.sort()
        cnt = 0
        for i in range(n):
            if time[i]>i:
                cnt+=1
            else:
                break
        return cnt
        