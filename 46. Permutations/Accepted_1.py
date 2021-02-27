from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # FYI- 순열 : 서로 다른 n개의 수에서 중복이 없게 r개를 택하여 일렬로 배열하는 것
        def dfs(index, path):
            if path is not None and len(path) == len(nums):
                result.append(path)
                return

            for i in range(index, len(nums)):
                for j in nums:
                    if j not in path:  # 중복되는 숫자가 없도록
                        dfs(i+1, path+[j])

        # 예외 처리 (입력값이 없을 떄)
        if nums is None:
            return []

        result = []
        dfs(0, [])
        return result


class Problem:
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))

    
'''
Runtime: 52 ms, faster than 16.07% of Python3 online submissions for Permutations.
Memory Usage: 14.4 MB, less than 46.67% of Python3 online submissions for Permutations.
'''
