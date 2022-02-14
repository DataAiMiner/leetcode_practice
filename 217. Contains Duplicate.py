class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = collections.Counter(nums)
        
        if len([cnt[k] for k in cnt if cnt[k] > 1]) == 0:
            return False
        
        return True
