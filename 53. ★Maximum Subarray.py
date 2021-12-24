# 출처 : https://siahn95.tistory.com/entry/AlgorithmLeetCodeEasyPython-53-Maximum-Subarray

# 해결 1 : Dynamic Programming (DP) - Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 맨 처음 원소로 변수 초기화
        current_subarray = max_subarray = nums[0]
        # 그 다음에 위치한 원소로 시작
        for num in nums[1:]:
            # current_subarray 가 음수면 버리고, 아니면 계속 더해 나간다.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

# 해결 2 : Divide and Conquer
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         def findBestSubarray(nums, left, right):
#             if left > right:
#                 return -math.inf

#             mid = (left + right) // 2
#             curr = best_left_sum = best_right_sum = 0
#             for i in range(mid - 1, left - 1, -1):
#                 curr += nums[i]
#                 best_left_sum = max(best_left_sum, curr)
                
#             curr = 0
#             for i in range(mid + 1, right + 1):
#                 curr += nums[i]
#                 best_right_sum = max(best_right_sum, curr)
#             best_combined_sum = nums[mid] + best_left_sum + best_right_sum
#             left_half = findBestSubarray(nums, left, mid - 1)
#             right_half = findBestSubarray(nums, mid + 1, right)
            
#             return max(best_combined_sum, left_half, right_half)
          
#         return findBestSubarray(nums, 0, len(nums) - 1)
