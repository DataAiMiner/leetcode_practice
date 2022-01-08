class Solution:
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
          
        ## OR
#         while head:
#             if head.val == None:
#                 return True
#             head.val = None
#             head = head.next
#         return False
