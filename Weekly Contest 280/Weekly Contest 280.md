## [2169. Count Operations to Obtain Zero](https://leetcode.com/contest/weekly-contest-280/problems/count-operations-to-obtain-zero/)
- [More concise solution](https://leetcode.com/problems/count-operations-to-obtain-zero/discuss/1766882/Python3-simulation)
```python3
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0 
        while num1 and num2: 
            ans += 1
            if num1 < num2: num1, num2 = num2, num1
            num1 -= num2
        return ans 
```
