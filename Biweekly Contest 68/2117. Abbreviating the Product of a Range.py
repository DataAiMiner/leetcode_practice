from functools import reduce  # Required in Python 3
import operator

class Solution:
    def prod(self, iterable):
        return reduce(operator.mul, iterable, 1)
    
    def abbreviateProduct(self, left: int, right: int) -> str:
        ### calculate
        # num = 1
        # for i in range(left, right+1):
        #     num *= i
        num = self.prod(range(left, right+1))
        # print(num)
        num_str = str(int(num))
        
        ### remove zeros in tail
        count_zero = 0
        for char in num_str[::-1]:
            if char == '0':
                count_zero += 1
            else:
                break
        if count_zero != 0:
            num_str = num_str[:-count_zero]
            
        ### refine length
        result = ''
        if len(num_str) > 10:
            result = num_str[:5] + '...' + num_str[-5:]
        else:
            result = num_str
        
        return result + 'e' + str(count_zero)
