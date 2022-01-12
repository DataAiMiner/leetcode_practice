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

## [2135. Count Words Obtained After Adding a Letter](https://leetcode.com/contest/weekly-contest-275/problems/count-words-obtained-after-adding-a-letter/)
- ord() : ASCII 코드 변환 함수 (ex)ord('a') : 97
- ^= : XOR 비트 연산(두 비트 중 하나만 1이면 각 비트를 1로 설정 후 할당) 후 할당 (ex)5^=3 : 6
- << : 비트 쉬프트 연산 (ex)a<<n : a*(2^n)
```python3
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords: 
            m = 0
            for ch in word: m ^= 1 << ord(ch)-97
            seen.add(m)
            
        ans = 0 
        for word in targetWords: 
            m = 0 
            for ch in word: m ^= 1 << ord(ch)-97
            for ch in word: 
                if m ^ (1 << ord(ch)-97) in seen: 
                    ans += 1
                    break 
        return ans 
```
