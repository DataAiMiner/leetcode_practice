class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        ind = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[ind] = nums[i+1]
                ind += 1
        return ind
