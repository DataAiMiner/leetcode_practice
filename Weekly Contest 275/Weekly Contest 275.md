# [Weekly Contest 275](https://leetcode.com/contest/weekly-contest-275/)

## [2133. Check if Every Row and Column Contains All Numbers](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/)
- [1-Liner Solution](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/discuss/1676835/Python3-1-line)
```python3
class Solution:
    def checkValid(self, mat: List[List[int]]) -> bool:
        return all(len(set(x)) == len(mat) for x in mat + list(zip(*mat)))
```
```python3
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(len(set(row)) == len(matrix) for row in matrix) and all(len(set(col)) == len(matrix) for col in zip(*matrix))
```
