from bisect import bisect

class Solution:
    def LIS(self, nums):
        dp = [10**10] * (len(nums) + 1)
        for elem in nums: dp[bisect(dp, elem)] = elem  
        return dp.index(10**10)
    
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # time : O(nlogn)
        # space : O(n)
        ans = 0
        for i in range(k):
            A = arr[i::k]
            ans += len(A) - self.LIS(A)
    
        return ans
