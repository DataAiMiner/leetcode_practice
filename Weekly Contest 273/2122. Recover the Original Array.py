import numpy as np

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        mid = int(len(nums)/2)
        
        lower = sorted_nums[:mid]
        higher = sorted_nums[mid:]
        
        k = int((higher[0] - lower[0])/2)
        sum_vector = np.array(lower) + np.array([k]*mid)
        
        return list(sum_vector)
