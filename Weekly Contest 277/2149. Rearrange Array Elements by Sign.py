class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        positive_nums = [num for num in nums if num>0]
        negative_nums = [num for num in nums if num<0]
        for i in range(len(positive_nums)):
            result.append(positive_nums[i])
            result.append(negative_nums[i])
        
        return result
