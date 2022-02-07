class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before_nums = [num for num in nums if num < pivot]
        pivot_nums = [num for num in nums if num == pivot]
        after_nums = [num for num in nums if num > pivot]
        return before_nums + pivot_nums + after_nums

## Faster Solution (https://leetcode.com/problems/partition-array-according-to-given-pivot/discuss/1747186/Python-3-array-solution)
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         left, right, piv = [], [], []
#         for n in nums:
#             if n < pivot:
#                 left.append(n)
#             elif n > pivot:
#                 right.append(n)
#             else:
#                 piv.append(n)
#         return left+piv+right
