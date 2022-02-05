class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## count all zeros
        N = collections.Counter(nums)[0]
        
        ## remove all zeros
        # nums = [num for num in nums if num != 0]
        while 0 in nums:
            nums.remove(0)
        
        ## append N zeros at the end
        extension = [0]*N
        nums.extend(extension)
        
        return nums
