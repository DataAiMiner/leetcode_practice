# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1648142/Python-Simple-2-Pass-O(N)-Solution-oror-Detailed-Explanation-oror-Beginner-Friendly

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        # forward
        pair = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                pair += 1
            else:
                pair -= 1
            if pair < 0:
                return False
        
        #
        pair = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                pair += 1
            else:
                pair -= 1
            if pair < 0:
                return False

        return True
