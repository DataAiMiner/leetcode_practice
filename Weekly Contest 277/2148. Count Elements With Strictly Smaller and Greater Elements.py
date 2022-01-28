class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        for each in nums:
            new_nums = nums[:]
            new_nums.remove(each)
            if max(new_nums) > each and min(new_nums) < each:
                count += 1
        
        return count
