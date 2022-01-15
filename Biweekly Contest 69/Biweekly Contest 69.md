## [2129.Capitalize the Title](https://leetcode.com/contest/biweekly-contest-69/problems/capitalize-the-title)
- Easy one, so passed.

## [2130. Maximum Twin Sum of a Linked List](https://leetcode.com/contest/biweekly-contest-69/problems/maximum-twin-sum-of-a-linked-list/)
- Easy one, passed, but look at the optimized approach below
- [time: O(N), space: O(1) optimized approach](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/discuss/1676025/Need-to-know-O(1)-space-solution-in-Python)
```python3
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            prev, curr = None, head
            while curr:
                next = curr.next
                curr.next = prev
                prev, curr = curr, next
            return prev
        
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = reverse(slow)
        max_so_far = 0
        
        while second:
            summ = first.val + second.val
            max_so_far = max(max_so_far, summ)
            first, second = first.next, second.next
        
        return max_so_far
```

## [2131.Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/contest/biweekly-contest-69/problems/longest-palindrome-by-concatenating-two-letter-words)
- [[Python] Simple O(N) Solution || Straightforward](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/discuss/1675386/Python-Simple-O(N)-Solution-oror-Straightforward)
- [Counting Mirror Words O(n)](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/discuss/1675343/Python3-Java-C%2B%2B-Counting-Mirror-Words-O(n))
- 
## [2132.Stamping the Grid](https://leetcode.com/contest/biweekly-contest-69/problems/stamping-the-grid)
- [2d cumulative sums, explained](https://leetcode.com/problems/stamping-the-grid/discuss/1675344/Python-2d-cumulative-sums-explained)
- [2D Range Sum Query | explained with images](https://leetcode.com/problems/stamping-the-grid/discuss/1675355/Python-or-2D-Range-Sum-Query-or-explained-with-images)
