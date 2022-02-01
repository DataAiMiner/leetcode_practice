### Time Limit Exceeded
# class Solution:
#     def maxScoreIndices(self, nums: List[int]) -> List[int]:        
#         score = 0
#         result = []
        
#         for i in range(len(nums)+1):
#             nums_left, nums_right = nums[:i], nums[i:]
#             pre_max = (i-sum(nums_left)) + sum(nums_right)
#             if pre_max > score:
#                 score, result = pre_max, [pre_max]
#             elif pre_max == score:
#                 result.append(pre_max)
            
#         return result

### Proper Solution
### Runtime: 3672 ms
### Memory Usage: 26.5 MB
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        score = 0
        result = []
        
        left = [0]
        count = 0
        for i in range(N):
            if nums[i] == 0:
                count += 1
            left.append(count)
            
        right = [0]
        count = 0
        for i in range(N-1, -1, -1):
            if nums[i] == 1:
                count += 1
            right.append(count)
        right = right[::-1]
        
        for i in range(N+1):
            pre_max = left[i] + right[i]
            if pre_max > score:
                score, result = pre_max, [i]
            elif pre_max == score:
                result.append(i)
        
        return result
