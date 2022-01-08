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


## Failed One
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         nodes = []
#         curr = head
#         prev = head
#         check_point = -1
#         while True:
#             if curr is None:
#                 return False
            
#             if curr.val in nodes:
#                 check_point = nodes.index(curr.val)
#                 print(check_point)
#                 print(nodes)
#                 print(curr.val, prev.val)
#                 if prev.val == nodes[check_point-1] or (prev.val == curr.val and curr.next is None):
#                     return True
#                 else:
#                     nodes.append(curr.val)
#             else:
#                 nodes.append(curr.val)
                
#             prev = curr
#             curr = curr.next
