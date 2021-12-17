class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                if n+m == target:
                    answer.append(i)
                    answer.append(j+(i+1))
                    return answer
