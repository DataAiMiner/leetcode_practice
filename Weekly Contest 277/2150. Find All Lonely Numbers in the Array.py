class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        
        result = []
        for num in nums:
            if cnt[num] < 2 and (cnt[num+1] == 0 and cnt[num-1] == 0):
                result.append(num)
        
        return result
