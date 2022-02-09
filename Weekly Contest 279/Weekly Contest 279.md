## [2164. Sort Even and Odd Indices Independently](https://leetcode.com/contest/weekly-contest-279/problems/sort-even-and-odd-indices-independently)

## [2165. Smallest Value of the Rearranged Number](https://leetcode.com/contest/weekly-contest-279/problems/smallest-value-of-the-rearranged-number)
- [Sort and Swap](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/discuss/1748511/Sort-and-Swap)
```python3
class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)), reverse = num < 0)
        non_zero = next((i for i, n in enumerate(s) if n != '0'), 0)
        s[0], s[non_zero] = s[non_zero], s[0]
        return int(''.join(s)) * (1 if num >= 0 else -1)
```
- [Easy and Concise with Explanation](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/discuss/1748527/Python-Easy-and-Concise-with-Explanation)
```python3
class Solution:
    def smallestNumber(self, a):
        s = sorted(str(abs(a)))
        if a <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))
```

## [2166. Design Bitset](https://leetcode.com/contest/weekly-contest-279/problems/design-bitset)

## [2167. Minimum Time to Remove All Cars Containing Illegal Goods](https://leetcode.com/contest/weekly-contest-279/problems/minimum-time-to-remove-all-cars-containing-illegal-goods)
