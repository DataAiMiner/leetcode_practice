class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-2) + f(n-1)
        f = {}
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i-2] + f[i-1]
        return f[n-1]
      

# Tabluation
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * (n + 1)        
#         # base cases
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
            
#         return dp.pop()
