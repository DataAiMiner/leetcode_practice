class Solution:
#   https://leetcode.com/problems/missing-number/discuss/69832/1%2B-lines-Ruby-Python-Java-C%2B%2B
#     def missingNumber(self, nums):
#       n = len(nums)
#       return n * (n+1) / 2 - sum(nums)
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N+1):
            if i not in nums:
                return i
