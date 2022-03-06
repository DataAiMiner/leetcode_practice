## [2194. Cells in a Range on an Excel Sheet](https://leetcode.com/contest/weekly-contest-283/problems/cells-in-a-range-on-an-excel-sheet)
- [Concise One](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/discuss/1823744/Two-Loops)
```python3
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(c) + chr(r) for c in range(ord(s[0]), ord(s[3]) + 1) for r in range(ord(s[1]), ord(s[4]) + 1)]
```
