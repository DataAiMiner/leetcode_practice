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
    
    
    def listToNode(self, pairs: list) -> ListNode:        
        head = tail = ListNode(pairs[0])
        i = 1
        while(i < len(pairs)):
            tail.next = ListNode(pairs[i])
            tail = tail.next
            i += 1
        return head
    
        
    def swapPairs(self, head: ListNode) -> ListNode:
        nodeList = self.nodeToList(head)
        if head is None or len(nodeList) < 2:
            return head
        
        if len(nodeList) % 2 == 1:
            for i in range(0, len(nodeList)-1, 2):
                nodeList[i], nodeList[i+1] = nodeList[i+1], nodeList[i]
        else:
            for i in range(0, len(nodeList), 2):
                nodeList[i], nodeList[i+1] = nodeList[i+1], nodeList[i]
        
        return self.listToNode(nodeList)
        
'''
Runtime: 52 ms, faster than 6.01% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.4 MB, less than 18.66% of Python3 online submissions for Swap Nodes in Pairs.
'''
