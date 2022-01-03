class Solution:
    def checkString(self, s: str) -> bool:
        
        if (s.find('a') == -1):
            # s consists of only b
            return True
        
        if (s.find('b') == -1):
            return True
        
        b_first = s.find('b')
        a_last = len(s) - s[::-1].find('a') - 1
        
        if b_first <= a_last:
            return False
        else:
            return True
