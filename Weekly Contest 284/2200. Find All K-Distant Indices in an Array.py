class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [i for i, num in enumerate(nums) if num == key]
        
        result = []
        for i, num in enumerate(nums):
            for key in keys:
                if abs(i-key) <= k:
                    result.append(i)
                    break
                    
        return result
