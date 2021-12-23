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
```python3
class Solution:
    def longestNonDecreasingSubsequence(self, arr):
        sub = []
        for i, x in enumerate(arr):
            if len(sub) == 0 or sub[-1] <= x:  # Append to LIS if new element is >= last element in LIS
                sub.append(x)
            else:
                idx = bisect_right(sub, x)  # Find the index of the smallest number > x
                sub[idx] = x  # Replace that number with x
        return len(sub)
    
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # Time Complexity : O(K * N/K * log(N/K)) = O(N * log(N/K))
        # Space Complexity : Time: O(K * N/K * log(N/K)) = O(N * log(N/K))
        n = len(arr)
        ans = 0
        for i in range(k):
            newArr = []
            for j in range(i, n, k):
                newArr.append(arr[j])
            ans += len(newArr) - self.longestNonDecreasingSubsequence(newArr)
        return ans
  ```

- [[Python] Short LIS, explained](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/discuss/1634978/Python-Short-LIS-explained)
