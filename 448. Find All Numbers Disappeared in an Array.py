class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        counter = collections.Counter(nums)
        # result = [n for n in range(1, N+1) if n not in nums] # -> results in Timeout
        result = [n for n in range(1, N+1) if counter[n] == 0]
        
        return result
      
## Another Solution from https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation
# def findDisappearedNumbers(self, nums):
#     for num in nums:
#         index = abs(num) - 1
#         nums[index] = -abs(nums[index])
            
#     return [i + 1 for i, num in enumerate(nums) if num > 0]
