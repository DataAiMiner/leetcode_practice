## [2138. Divide a String Into Groups of Size k](https://leetcode.com/contest/weekly-contest-276/problems/divide-a-string-into-groups-of-size-k)
- Easy, so pass.

## [2139. Minimum Moves to Reach Target Score](https://leetcode.com/contest/weekly-contest-276/problems/minimum-moves-to-reach-target-score)
- Easy, so pass.
- [can also use recursion](https://leetcode.com/problems/minimum-moves-to-reach-target-score/discuss/1694523/EZ-Python-Code-For-Beginners-Using-Recursion)
```python3
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target==1:
            return 0
        if maxDoubles==0:
            return target-1
        if target & 1==1:
            return 1+self.minMoves(target-1,maxDoubles)
        else:
            return 1+self.minMoves(target//2,maxDoubles-1)
```
- [or simple as this](https://leetcode.com/problems/minimum-moves-to-reach-target-score/discuss/1693327/JavaC%2B%2BPython-Reduce-target-to-1)
```python
def minMoves(self, target, k):
        res = 0
        while target > 1 and k > 0:
            res += 1 + target % 2
            k -= 1
            target >>= 1
        return target - 1 + res
```

## [2140. Solving Questions With Brainpower](https://leetcode.com/contest/weekly-contest-276/problems/solving-questions-with-brainpower)
- [Dynamic Programming](https://leetcode.com/problems/solving-questions-with-brainpower/discuss/1692963/DP)
```python3
class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            return 0 if i >= len(q) else max(dfs(i + 1), q[i][0] + dfs(i + 1 + q[i][1]))
        return dfs(0)
```
```python3
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)
        max_score = 0
        i = len(questions) - 1
        while i >= 0:
            point, brainpower = questions[i]
            dp[i] = max(max_score, point + dp[i+brainpower+1])
            max_score = max(max_score, dp[i])
            i -= 1
        return max_score
```


## [2141. Maximum Running Time of N Computers](https://leetcode.com/contest/weekly-contest-276/problems/maximum-running-time-of-n-computers)
