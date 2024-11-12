from typing import List

class Solution:
    def customBinarySearch(self, items: List[List[int]], queryPrice: int) -> int:
        l = 0
        r = len(items) - 1
        maxBeauty = 0

        while l <= r:
            mid = l + (r - l) // 2

            if items[mid][0] > queryPrice:
                r = mid - 1  # Ignore current and right side items, move to left.
            else:
                maxBeauty = max(maxBeauty, items[mid][1])
                l = mid + 1

        return maxBeauty

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        m = len(queries)
        result = [0] * m

        # Step-1: Sort the array based on price in ascending order
        items.sort()  # items = [[price_i, beauty_i]]

        # Update items to store the maximum beauty seen so far for each price
        maxBeautySeen = items[0][1]
        for i in range(1, n):
            maxBeautySeen = max(maxBeautySeen, items[i][1])
            items[i][1] = maxBeautySeen

        # Perform a binary search for each query to find the maximum beauty
        for i in range(m):
            queryPrice = queries[i]
            result[i] = self.customBinarySearch(items, queryPrice)

        return result
