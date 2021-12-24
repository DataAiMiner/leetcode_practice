from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)
        minimum = min(counted, key=counted.get)
        
        return minimum
