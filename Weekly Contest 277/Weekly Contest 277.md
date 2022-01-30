## [2148. Count Elements With Strictly Smaller and Greater Elements](https://leetcode.com/contest/weekly-contest-277/problems/count-elements-with-strictly-smaller-and-greater-elements)
- [Easy O(N) Solution | O(1) Space](https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/discuss/1711489/Python-Easy-O(N)-Solution)
```python3
class Solution:
    def countElements(self, nums: List[int]) -> int:
        lo, hi = min(nums), max(nums)
        return sum(1 for x in nums if lo<x<hi)
```

## [2149. Rearrange Array Elements by Sign](https://leetcode.com/contest/weekly-contest-277/problems/rearrange-array-elements-by-sign)
```python3
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        return [i for t in zip([p for p in nums if p > 0], [n for n in nums if n < 0]) for i in t]
```

## [2150. Find All Lonely Numbers in the Array](https://leetcode.com/contest/weekly-contest-277/problems/find-all-lonely-numbers-in-the-array)
- [Simplified Counter](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/discuss/1711316/Counter)
```python3
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        return [n for n in nums if m[n] == 1 and m[n - 1] + m[n + 1] == 0]
```

## [2151. Maximum Good People Based on Statements](https://leetcode.com/contest/weekly-contest-277/problems/maximum-good-people-based-on-statements)
