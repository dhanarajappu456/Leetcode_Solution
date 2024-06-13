import heapq as h 
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        h.heapify(seats)
        ans = 0
        for pos in sorted(students):
            ans+= abs(pos-h.heappop(seats))
        return ans