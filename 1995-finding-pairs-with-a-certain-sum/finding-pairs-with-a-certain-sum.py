from collections import defaultdict as dict 
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        #create the map to create the count of num in the second aray 
        self.map1 = dict(int)
        self.map2   = dict(int)
        self.nums1 = nums1
        self.nums2 = nums2
        for num in  nums2:
            
            self.map2[num]+=1
        for num in nums1:
            self.map1[num]+=1

        #print(self.map1, self.map2)

        

    def add(self, index: int, val: int) -> None:
        #when adding a value to number update the map ,
        #in a way that old number count is dec and the new one is added 
        old_val = self.nums2[index]
        self.nums2[index]+=val 
        new_val = self.nums2[index]
        self.map2[old_val]-=1
        self.map2[new_val]+=1

    def count(self, tot: int) -> int:
        #get the count in const time 
        #print("be", self.nums1, self.nums2)
        cnt  =0 
        for num in self.map1:
            if tot - num in self.map2:
                cnt+= (self.map1[num] * self.map2[tot-num])
        return cnt 
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)