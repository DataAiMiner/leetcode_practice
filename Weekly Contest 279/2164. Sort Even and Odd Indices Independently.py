class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        
        N = len(nums)//2
        
        even_nums = sorted([num for i, num in enumerate(nums) if i % 2 == 0], reverse=True)
        odd_nums = sorted([num for i, num in enumerate(nums) if i % 2 != 0])
        
        result = []
        for i in range(N):
            result.append(even_nums.pop())
            result.append(odd_nums.pop())
        
        if len(even_nums) > 0:
            result.append(even_nums.pop())
        if len(odd_nums) > 0 :
            result.append(odd_nums.pop())
        
        return result
      
## More concise & faster solution (https://leetcode.com/problems/sort-even-and-odd-indices-independently/discuss/1748551/Python-Two-lines)
# class Solution:
#     def sortEvenOdd(self, A):
#         A[::2], A[1::2] = sorted(A[::2]), sorted(A[1::2])[::-1]
#         return A
