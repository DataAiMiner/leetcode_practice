## [2124. Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)
- [1 Liner Solution](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/discuss/1661056/Python-1-Liner)
```python3
class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
```

## [2125. Number of Laser Beams in a Bank](https://leetcode.com/contest/weekly-contest-274/problems/number-of-laser-beams-in-a-bank)
- [[Python3, Java, C++] Simple O(mn)](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/discuss/1660943/Python3-Java-C%2B%2B-Simple-O(mn))

## [2126. Destroying Asteroids](https://leetcode.com/contest/weekly-contest-274/problems/destroying-asteroids)
- [Sort then apply greedy algorithm.](https://leetcode.com/problems/destroying-asteroids/discuss/1661044/JavaPython-3-Sort-then-apply-greedy-algorithm.)
```python3
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True
```

## [2127. Maximum Employees to Be Invited to a Meeting](https://leetcode.com/contest/weekly-contest-274/problems/maximum-employees-to-be-invited-to-a-meeting)
