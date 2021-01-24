# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodeToList(self, node) -> list:
        lst = []
        while(node):
            lst.append(node.val)
            node = node.next
        return lst
    
    
    def listToNode(self, arr) -> ListNode:
        print(arr)
        head = ListNode(arr[0])
        tail = head
        i = 1
        while i < len(arr):
            tail.next = ListNode(arr[i])
            tail = tail.next
            i += 1
        return head
        
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        rev = self.nodeToList(head)
        rev.reverse()
        revNode = self.listToNode(rev)
        return revNode
