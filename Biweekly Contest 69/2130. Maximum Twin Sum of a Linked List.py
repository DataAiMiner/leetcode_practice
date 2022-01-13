# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def toList(self, origin: Optional[ListNode]):
        result = []
        head = origin
        while head is not None:
            result.append(head.val)
            head = head.next
        return result
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        listed = self.toList(head)
        n = len(listed)
        
        if n == 2:
            return sum(listed)
        
        med = len(listed)//2
        maximum = 0
        for i in range(med, n):
            maximum = max(maximum, listed[i]+listed[n-1-i])
        
        return maximum
