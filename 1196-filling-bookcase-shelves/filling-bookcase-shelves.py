from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # Memoization dictionary to store intermediate results
        memo = {}
        #function computes minheight to keep all books form i to n
        def rec(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            
            width = 0
            height = 0
            min_height = float('inf')
            
            # Try placing as many books as possible on the current shelf
            for j in range(i, n):
                if width + books[j][0] > shelfWidth:
                    break
                width += books[j][0]
                height = max(height, books[j][1])
                min_height = min(min_height, height + rec(j + 1))
            
            memo[i] = min_height
            return min_height
        
        return rec(0)
