class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [ True for i in range(1000+1)]
        primes[0] = False
        primes[1] = False
        for i in range(2, 1001):
            for j in range(i+1,1001):
                if j%i == 0:
                    primes[j] = False 
        def find_next_prime(num):
            for i in range(num, 1000+1):
                if primes[i] ==True:
                    return i
            return -1

        #once we have the sieve array for the primes
        #we start from the end and 
        #if the current element at index i greater than
        #i+1 , reduce the current element
        #at index i  
        #by a prime number p > d , where d id the diff b/e nums[i]
        #nums [i+1]
        n = len(nums)
        for i in range(n-2,-1,-1 ):
            if nums[i]>=nums[i+1]:
                diff = nums[i] - nums[i+1]
                ans = find_next_prime(diff+1)
                if ans  == -1 :
                    return False
                nums[i]-= ans 
                if nums[i]<1:
                    return False 
        return True


