class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if i == 0 and n > target:
                return 0
            if i == len(nums)-1:
                if n == target:
                    return i
                elif n < target:
                    return i+1
                elif n > target:
                    return 0
            if n == target:
                return i
            if n < target and nums[i+1] > target:
                return i+1
