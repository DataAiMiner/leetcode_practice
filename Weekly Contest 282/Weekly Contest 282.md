## [2186. Minimum Number of Steps to Make Two Strings Anagram II](https://leetcode.com/contest/weekly-contest-282/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/)
- [Counter](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/discuss/1802805/Counter)
```python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        return sum(cnt for ch, cnt in ((cs - ct) + (ct - cs)).items())
```
