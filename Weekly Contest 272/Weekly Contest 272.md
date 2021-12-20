## [2110. Number of Smooth Descent Periods of a Stock](https://leetcode.com/contest/weekly-contest-272/problems/number-of-smooth-descent-periods-of-a-stock/)

#### Dynamic Programming
- [[Python] short dp, explained](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/discuss/1635000/Python-short-dp-explained)
```python3
  class Solution:
      def getDescentPeriods(self, P):
          n = len(P)
          dp = [1]*n
          for i in range(1, n):
              if P[i] == P[i-1] - 1:
                  dp[i] = 1 + dp[i-1]
                
          return sum(dp)
  ```
- [[Python] Explanation with pictures.](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/discuss/1635104/Python-Explanation-with-pictures.)

## [2111. Minimum Operations to Make the Array K-Increasing](https://leetcode.com/contest/weekly-contest-272/problems/minimum-operations-to-make-the-array-k-increasing/)
#### LIS
- [[C++/Python] Longest Non-Decreasing Subsequence - Clean & Concise](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/discuss/1635013/C%2B%2BPython-Longest-Non-Decreasing-Subsequence-Clean-and-Concise)
- [[Python] Short LIS, explained](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/discuss/1634978/Python-Short-LIS-explained)
