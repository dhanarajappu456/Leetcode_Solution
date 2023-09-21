class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        #binary search on smallest array to avoid out of bounds
        #Eg: nums1 = [2,3,4,5,6], nums2=  [1]
        nums1, nums2 = (nums1, nums2) if len(
            nums1) <= len(nums2) else (nums2, nums1)

        firstLen, secondLen = len(nums1), len(nums2)
        low, high = 0, firstLen-1
        res = 0
        while (True):

            cut1 = (low+high)//2
            cut2 = (firstLen+secondLen-1)//2 - (cut1+1)

            l1 = float("-inf") if cut1 < 0 else nums1[cut1]
            r1 = float("inf") if cut1+1 >= firstLen else nums1[cut1+1]
            l2 = float("-inf") if cut2 < 0 else nums2[cut2]
            r2 = float("inf") if cut2+1 >= secondLen else nums2[cut2+1]

            if l1 > r2:
                high -= 1
            elif l2 > r1:
                low += 1

            else:
               
                res = [max(l1, l2), (max(l1, l2)+min(r1, r2)) /
                       2][(firstLen+secondLen) % 2 == 0]
                break
        return res
