'''
#solution 1 -bruteforc
#solution2 - fisher yates - algo

'''
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.temp = nums.copy()
    
      
        

    def reset(self) -> List[int]:
        
        self.nums = self.temp.copy()
      
        return self.nums
        

    def shuffle(self) -> List[int]:
        
        n = len(self.nums)
        arr = self.nums[:]
        for i in range(n):
            rand_ind  = random.randint(0,len(arr)-1)
            self.nums[i] = arr[rand_ind]
            arr.pop(rand_ind)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()