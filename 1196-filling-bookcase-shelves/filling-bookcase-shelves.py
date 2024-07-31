from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # Memoization dictionary to store intermediate results
        memo = {}
        #this keeps minheight to keep books from i to n with rem_widht_prev as the widht of shelf in which prev
        #book is kept  and max_heigt of the  same
        def rec(i,rem_width_prev,max_height_prev ):
            if i == n:
                return max_height_prev
            #note we need to cache only i and rem_width_prev, becaue when
            #i and rem_width_prev is same , the max_height_prev also will be same
            #as is the max_heihg of prev_shelf, and also the books are kept in order,
            #and same i  and rem_width_prev means same set of books in the prev shelf no matter what
            if (i,rem_width_prev) in memo:
                return memo[(i,rem_width_prev)]
            w,h = books[i]
            take_current = float("inf")
            #you can keep the book at same shelf as prev book
            if rem_width_prev>=w:
                take_current = rec(i+1,rem_width_prev-w, max(h,max_height_prev))
            #can skip the prev_shelf , when skipping, we need add the prev_shelf_height , as height increase now
            skip_current = max_height_prev + rec(i+1,shelfWidth-w, h)
            memo[(i,rem_width_prev)]=  min(take_current,skip_current )
            return memo[(i,rem_width_prev)]

        return rec(0,shelfWidth,0)
