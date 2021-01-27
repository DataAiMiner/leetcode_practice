# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodeToList(self, node: ListNode) -> list:
        result = []
        while(node):
            result.append(node.val)
            node = node.next
        return result
    
    
    def listToNode(self, result: list) -> ListNode:
        head = tail = ListNode(result[0])
        i = 1
        while(i < len(result)):
            tail.next = ListNode(result[i])
            tail = tail.next
            i += 1
        return head        
        
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        nodeList = self.nodeToList(head)
        if head is None or len(nodeList) <= 2:
            return head
        evenList = []
        oddList = []
        for i in range(0, len(nodeList)):
            if (i % 2 == 1):
                evenList.append(nodeList[i])
            else:
                oddList.append(nodeList[i])
        
        return(self.listToNode(oddList+evenList))
        
'''
Runtime: 100 ms, faster than 5.60% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 17.6 MB, less than 5.00% of Python3 online submissions for Odd Even Linked List.
''' 
