class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count, ans, n = collections.Counter(), 0, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                ans += 8 * count[nums[i]*nums[j]]
                count[nums[i]*nums[j]] += 1
        return ans
        
'''
a * b = c * d; there are 8 permutations of tuples for every (a,b,c,d) that satisfy this 
i.e (a,b,c,d), (a,b,d,c), (b,a,c,d), (b,a,d,c), (c,d,a,b), (c,d,b,a), (d,c,a,b), (d,c,b,a). 
So for every two pairs (a,b) and (c,d) that have the same product, we have 8 tuples and hence 
whenever we find a tuple (a,b) we check how many other (c,d) are present with the same product, 
for each of these same product (c,d) there are 8 tuples. Hence 8 * number of tuples that have the same product.

https://leetcode.com/problems/tuple-with-same-product/discuss/1020621/Simple-Python3-or-6-Lines-or-Detailed-Explanation
https://leetcode.com/problems/tuple-with-same-product/discuss/1020657/Python3-freq-table
'''
