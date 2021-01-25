# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listToNode(self, resultList: list) -> ListNode:
        head = tail = ListNode(resultList[0])
        i = 1
        while(i < len(resultList)):
            tail.next = ListNode(resultList[i])
            tail = tail.next
            i += 1
        return head
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0
        resultList = []
        while(l1 and l2) :
            sum = 0
            if left == 1:
                sum = 1
            left = 0
            
            sum += l1.val + l2.val
            
            if sum >= 10 :
                sum = sum - 10
                left = 1
            resultList.append(sum)
            l1, l2 = l1.next, l2.next
            
        # add left elems
        if l1:
            while(l1):
                sum = 0
                if left == 1:
                    sum = 1
                left = 0
                sum += l1.val
                if sum >= 10 :
                    sum = sum - 10
                    left = 1
                resultList.append(sum)
                l1 = l1.next
                
        if l2:
            while(l2):
                sum = 0
                if left == 1:
                    sum = 1
                left = 0
                sum += l2.val
                if sum >= 10 :
                    sum = sum - 10
                    left = 1
                resultList.append(sum)
                l2 = l2.next
        
        if left == 1:
            resultList.append(1)
        result = self.listToNode(resultList)
        return result
        
'''
Runtime: 72 ms, faster than 50.94% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 44.44% of Python3 online submissions for Add Two Numbers.
'''
