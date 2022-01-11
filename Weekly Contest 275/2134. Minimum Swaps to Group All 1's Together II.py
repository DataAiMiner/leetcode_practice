class Solution:
    def minSwaps(self, nums: List[int]) -> int:
      
        num_one = sum(nums)
        lo = -1
        mx = ones = 0
        N = len(nums)
        
        for i in range(2*N):
            ones += nums[i % N]
            if i - lo > num_one:
                lo += 1
                ones -= nums[lo % N]
            mx = max(mx, ones)
            
        return num_one-mx
