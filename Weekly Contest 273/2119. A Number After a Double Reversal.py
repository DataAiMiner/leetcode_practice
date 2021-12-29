class Solution:
    def removeZeroFronts(self, num_str):
        for i, char in enumerate(num_str):
            if char != '0':
                return num_str[i:]
    
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        
        origin_num_str = str(num)
        reversed1 = self.removeZeroFronts("".join(reversed(origin_num_str)))
        reversed2 = self.removeZeroFronts("".join(reversed(reversed1)))
        
        if origin_num_str != reversed2:
            return False
        else:
            return True
