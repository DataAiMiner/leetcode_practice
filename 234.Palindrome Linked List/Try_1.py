# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNext(self, head, total_list):
        if (head is not None):
            total_list.append(head.val)
            self.getNext(head.next, total_list)
        return total_list
    
    def isPalindrome(self, head: ListNode) -> bool:
        # print(head.val)
        # print(head.next.val)
        # 이번 값과 다음 값이 동일할 때까지 찾는다.
        # 그 시점이 나오지 않으면 False, 그 시점이 나오면 그 index를 기준으로

        # 1. List로 받는다
        total_list = []
        total_list = self.getNext(head, total_list)
        
        if (len(total_list) == 0 or len(total_list) == 1):
            return True
        
        # 2. 대칭이라면 가져야 할 조건 체크
        '''
        1. total_list의 길이가 (symmetric_ind*2) +1 만큼이어야 한다.
        2. symmetric_ind로부터
        '''
        symmetric_ind = 0  # 대칭이 시작되는 ind - 1
        for i in range(0, len(total_list)-1):
            if total_list[i] == total_list[i+1]:
                symmetric_ind = i
        print(symmetric_ind)
        if (len(total_list) == (symmetric_ind+1)*2):
            distance = 1
            for i in range(symmetric_ind, -1, -1):
                print(total_list[i])
                if total_list[i] == total_list[symmetric_ind + distance]:
                    distance += 1
                    continue
                else:
                    return False
            return True
        else:
            return False
        
        
